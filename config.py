import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
TARGET_WALLET = os.getenv("TARGET_WALLET")

