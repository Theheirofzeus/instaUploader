from pyrogram import filters
from Bot import app
from .insta import 

async def start(client, message):
    await message.reply("Hello imma downloader")

app.add_handler(MessageHandler(filters.command("start")))
app.add_handler(MessageHandler(filters.command("start")))
app.run()
