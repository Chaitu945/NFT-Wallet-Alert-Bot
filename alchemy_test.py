import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALCHEMY_API_KEY")

url = f"https://eth-mainnet.g.alchemy.com/v2/{API_KEY}"

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "eth_blockNumber",
    "params": []
}

response = requests.post(url, json=payload)

print(response.json())