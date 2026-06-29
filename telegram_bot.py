from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(BOT_TOKEN)


async def send_alert(message, photo=None):

    if photo:
        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=photo,
            caption=message
        )
    else:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )