import requests
from config import ALCHEMY_API_KEY


def latest_block():

    url = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"

    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }

    r = requests.post(url, json=payload)

    return r.json()


def get_latest_nft_transfer(wallet):

    url = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "alchemy_getAssetTransfers",
        "params": [
            {
                "fromBlock": "0x0",
                "toBlock": "latest",
                "toAddress": wallet,
                "category": [
                    "erc721",
                    "erc1155"
                ],
                "withMetadata": True,
                "maxCount": "0x14",
                "order": "desc"
            }
        ]
    }

    r = requests.post(url, json=payload)

    return r.json()


def get_transaction_receipt(tx_hash):

    url = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_getTransactionReceipt",
        "params": [tx_hash]
    }

    r = requests.post(url, json=payload)

    return r.json()

def get_collection_name(contract_address):

    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{ALCHEMY_API_KEY}/getContractMetadata"

    params = {
        "contractAddress": contract_address
    }

    r = requests.get(url, params=params)

    return r.json()

def get_nft_metadata(contract_address, token_id):

    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{ALCHEMY_API_KEY}/getNFTMetadata"

    params = {
        "contractAddress": contract_address,
        "tokenId": token_id
    }

    r = requests.get(url, params=params)

    return r.json()









""" import requests
from config import ALCHEMY_API_KEY
def get_transaction_receipt(tx_hash):

    url = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_getTransactionReceipt",
        "params": [tx_hash]
    }

    r = requests.post(url, json=payload)

    return r.json()    """