import requests
import pyrogram 
from pyrogram import filters, Message
from Bot import app

@app.on_message(filters.command("insta|Insta|INSTA"))
def instadownloader(message):
    url = "https://instagram-media-downloader.p.rapidapi.com/tgbots/ig/load/post.php"
    message = update.effective_message
    user = update.effective_user
    search = message.text.split(' ', 1)
    if len(search) == 1:
        update.effective_message.reply_text('Format: "/insta videolink"')
        return
    else:
        search = search[1]
        querystring = {"url":"{search}"}
        headers = {
        'x-rapidapi-host': "instagram-media-downloader.p.rapidapi.com",
        'x-rapidapi-key': "2051122955msh62135c6dfc4b8c6p1408d0jsn0baf0aff3796"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    video = json.loads(response.text)
    videoo = video['image']
    captain = video['caption']
    message.reply.send_video(videoo, captain)




