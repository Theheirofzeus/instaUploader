from pyrogram import filters
from Bot import app

@app.on_message(filters.private|filters.command("start"))
async def start(client, message):
    await message.reply("Hello imma downloader")


app.run()
