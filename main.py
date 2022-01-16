from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
from pyrogram import Client, filters
import os 
session_name = os.environ.get("SESSION")
api_id = os.environ.get("API_ID")
api_hash =os.environ.get("API_HASH")
app = Client(session_name, api_id, api_hash,"pyro")


@app.on_message(filters.private|filters.command("start"))
async def start(client, message):
    await message.reply("Hello imma downloader")


app.run()