import requests
from config import ALCHEMY_API_KEY

def latest_block():

    url = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"

    payload = {
        "jsonrpc":"2.0",
        "method":"eth_blockNumber",
        "params":[],
        "id":1
    }

    r = requests.post(url, json=payload)

    return r.json()