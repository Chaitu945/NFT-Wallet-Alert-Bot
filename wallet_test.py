import requests
from config import ALCHEMY_API_KEY, TARGET_WALLET

url = (
    f"https://eth-mainnet.g.alchemy.com/nft/v3/"
    f"{ALCHEMY_API_KEY}/getNFTsForOwner"
)

params = {
    "owner": TARGET_WALLET,
    "withMetadata": "true",
    "pageSize": 5
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())