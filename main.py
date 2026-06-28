import asyncio

from telegram_bot import send_alert
from alchemy import latest_block

async def main():

    block = latest_block()

    await send_alert(f"Latest Block:\n\n{block}")

asyncio.run(main())


