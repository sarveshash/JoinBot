from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated

API_KEY = 20058505
API_HASH = "c6416428be72db3174999c1740524b88"
BOT_TOKEN = "6563744619:AAG4v_ABfLA3lCSGbcNLWlS07ZA_qUmseqM"

app = Client("app name",api_id=API_KEY,api_hash=API_HASH,bot_token=BOT_TOKEN)

@app.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " Hello,Welcome!\nI was created by my master SARVESH !")

@app.on_message(filters.command('help'))
def command2(bot,message):
    message.reply_text(" Help Section")


GROUP = "demoexample"
WELCOME_MESSAGE = "HI,WELCOME TO THE GROUP"

@app.on_message(filters.chat(GROUP)&filters.new_chat_members)
def command4(client, message):
    message.reply_text(WELCOME_MESSAGE)

#send photo
@app.on_message(filters.command('photo'))
def command5(bot, message):
    bot.send_photo(message.chat.id, "https://i.kinja-img.com/image/upload/c_fill,h_675,pg_1,q_80,w_1200/e8aa43862b64696a9ba03b6d69a882be.jpg")
    bot.send_photo(message.chat.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNh5h68CGoCiFOdg3XawGky8vBOzz2gjN9gg&usqp=CAU")

#send audio
@app.on_message(filters.audio & filters.private)
def audio(bot, message):
    message.reply_text(message.audio.file_id) #get the audio link

@app.on_message(filters.command('audio'))
def command6(bot, message):
    bot.send_audio(message.chat.id, "CQACAgUAAxkBAAPIZe24rC1Y6LJR_DaspVpGygPf0ekAAtMOAALepmhXQq-80lFCZYEeBA") #send the audio file

#send document
@app.on_message(filters.document & filters.private)
def document(bot, message):
    message.reply_text(message.document.file_id) #get the document id

@app.on_message(filters.command('file'))
def command7(bot, message):
    bot.send_document(message.chat.id, "BQACAgUAAxkBAAIBAWXtxPKFhdtS85bJ0Qa70XNsOUanAAImDwAC3qZoVxJY32wB-KacHgQ")

#send sticker
@app.on_message(filters.sticker & filters.private)
def sticker(bot, message):
    message.reply_text(message.sticker.file_id) #get the sticker id

@app.on_message(filters.command('sticker'))
def command8(bot, message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIBBWXtxjvvm6S4Hok9JWppe5F0Q2vSAAIQAQACUomRI8RI8frMHAbzHgQ")

#send video
@app.on_message(filters.video & filters.private)
def video(bot, message):
    message.reply_text(message.video.file_id) #get the video id

@app.on_message(filters.command('video'))
def command9(bot, message):
    bot.send_video(message.chat.id, "BAACAgEAAxkBAAIBCmXtx5sg15yUv8UWzcGlu6Lu9UiSAAKPAAMFrylFvSJs7TptjcMeBA") 

# send voice
@app.on_message(filters.voice & filters.private)
def voice(bot, message):
    message.reply_text(message.voice.file_id) #get the voice id

@app.on_message(filters.command('voice'))
def command9(bot, message):
    bot.send_voice(message.chat.id, "CgACAgQAAxkBAAIBHWXtySQ3jSvgHVRp4M1mhJ5E_s8RAAKcBAACkDKkUZ9RIf9wIzrdHgQ")
print("Hello")
@app.on_message(filters.text)
def delete (bot, message):
    word_list = ["Promotion"]
    if message.text in word_list:
        bot.delete_messages(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Blocklisted Word")
print("I am running")
@app.on_message(filters.command('bot_version'), group=2)
def version (bot, message):
    bot.send_message(message.chat.id, "Bot Version ~ 1.1")
print("I AM ALIVE")

app.run()
