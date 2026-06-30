import asyncio
import json

from telegram_bot import send_alert
from config import TARGET_WALLET
from alchemy import get_latest_nft_transfer
from alchemy import get_collection_info, get_floor_price
from transaction import classify_transaction


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

            info = get_collection_info(contract)

            collection = info["name"]
            floor = get_floor_price(contract)
            slug = info["slug"]
            photo = info["image"]

            count = len(tx_transfers)

            if count == 0:
                continue

            if isinstance(floor, (int, float)):
                floor_text = f"{floor} ETH"
            else:
                floor_text = "N/A"
            

            tx_info = classify_transaction(tx_hash)

            tx_type = tx_info["type"]

            marketplace = tx_info["marketplace"]

            title = "🐋 NFT PURCHASE" if tx_type == "PURCHASE" else "📥 NFT RECEIVED"
            

            message = (
                f"{title}\n\n"
                f"🎨 Collection: {collection}\n\n"
                f"🏪 Marketplace: {marketplace or 'N/A'}\n\n"
                f"📦 NFTs {'Bought' if tx_type == 'PURCHASE' else 'Received'}: {count}\n\n"
            )

            if floor is not None:
                message += f"💎 Floor: {floor} ETH\n\n"

            
            if slug:
                message += (
                    f"🌊 OpenSea:\n"
                    f"https://opensea.io/collection/{slug}\n\n"
                )

            message += (
                f"🔗 Transaction:\n"
                f"https://etherscan.io/tx/{tx_hash}"
            )
         

            try:
                if photo:
                    await send_alert(message, photo)
                else:
                    await send_alert(message)

            except Exception as e:
                print(f"Telegram photo failed: {e}")

                await send_alert(message)

        state["processed"] = list(processed)[-100:]

        save_state(state)

        await asyncio.sleep(10)

