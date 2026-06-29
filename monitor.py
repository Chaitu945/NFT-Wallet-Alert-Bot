import asyncio
import json

from telegram_bot import send_alert
from config import TARGET_WALLET
from alchemy import get_latest_nft_transfer
from alchemy import get_collection_name
from alchemy import get_nft_metadata


STATE_FILE = "state.json"


def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {"processed": []}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


async def monitor():

    state = load_state()
    processed = set(state.get("processed", []))

    while True:

        result = get_latest_nft_transfer(TARGET_WALLET)

        transfers = result["result"]["transfers"]

        if not transfers:
            await asyncio.sleep(10)
            continue

        grouped = {}

        for transfer in transfers:

            tx = transfer["hash"]

            if tx not in grouped:
                grouped[tx] = []

            grouped[tx].append(transfer)

        for tx_hash, tx_transfers in grouped.items():

            if tx_hash in processed:
                continue

            processed.add(tx_hash)

            contract = tx_transfers[0]["rawContract"]["address"]

            collection_data = get_collection_name(contract)
            collection = collection_data.get("openSeaMetadata", {}).get(
                "collectionName",
                collection_data.get("name", "Unknown Collection")
            )

            floor = collection_data.get("openSeaMetadata", {}).get("floorPrice")

            if floor is None:
                floor = "N/A"
            

            slug = collection_data.get("openSeaMetadata", {}).get(
                "collectionSlug",
                ""
            )

            nft_names = []
            photo = None

            for i, t in enumerate(tx_transfers):

                try:
                    nft = get_nft_metadata(
                        t["rawContract"]["address"],
                        t["tokenId"]
                )
                except Exception as e:
                    print(f"Metadata error: {e}")
                    continue

                name = nft.get("name")

                if not name or name.lower() == collection.lower():
                    name = f"#{int(t['tokenId'], 16)}"

                nft_names.append(name)

                if i == 0:
                    photo = nft.get("image", {}).get("pngUrl")

                    if not photo:
                        photo = nft.get("image", {}).get("cachedUrl")
            

            if isinstance(floor, (int, float)):
                floor_text = f"{floor} ETH"
                est_value = round(floor * len(nft_names), 4)
                est_value_text = f"{est_value} ETH"
            else:
                floor_text = "N/A"
                est_value_text = "N/A"

            if not nft_names:
                continue
            

            message = (
    f"🚨 NFT SWEEP\n\n"
    f"🎨 Collection: {collection}\n\n"
    f"📦 NFTs Bought: {len(nft_names)}\n\n"
    f"💎 Floor: {floor_text}\n\n"
    f"💰 Est. Floor Value: {est_value_text}\n\n"
    f"🏷 NFTs\n"
    f"{chr(10).join('• ' + x for x in nft_names)}\n\n"
    f"🌊 OpenSea:\n"
    f"https://opensea.io/collection/{slug}\n\n"
    f"🔗 Transaction:\n"
    f"https://etherscan.io/tx/{tx_hash}"
)
         

            if photo:
                await send_alert(message, photo)
            else:
                await send_alert(message)

        state["processed"] = list(processed)[-100:]

        save_state(state)

        await asyncio.sleep(10)

