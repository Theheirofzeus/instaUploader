
from pyrogram import Client, filters
import os 
bot_token = os.environ.get("TOKEN")
api_id = os.environ.get("API_ID")
api_hash =os.environ.get("API_HASH")
app = Client(session_name="pyro", bot_token=bot_token, api_id=api_id, api_hash=api_hash)

