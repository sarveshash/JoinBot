import asyncio
from logging import getLogger
from JOINBOT import *
from pyrogram import *
from pyrogram.types import *

LOG = getLogger(__name__)
loop = asyncio.get_event_loop()

async def main():
    LOG.info('starting....')
    await app.start()
    await app.send_message(-1002046949026,'started')
    LOG.info('started')
    await idle()
    await app.stop()
    


@app.on_message(filters.command('start') & filters.private)
async def command1(bot,message):
    await bot.send_message(message.chat.id, " Hello,Welcome!\nI was created by my master SARVESH !")

@app.on_message(filters.command('help'))
async def command2(bot,message):
    await message.reply_text(" Help Section")


GROUP = "demoexample"
WELCOME_MESSAGE = "HI,WELCOME TO THE GROUP"

@app.on_message(filters.chat(GROUP)&filters.new_chat_members)
async def command4(client, message):
    await message.reply_text(WELCOME_MESSAGE)

#send photo
@app.on_message(filters.command('photo'))
async def command5(bot, message):
    await bot.send_photo(message.chat.id, "https://i.kinja-img.com/image/upload/c_fill,h_675,pg_1,q_80,w_1200/e8aa43862b64696a9ba03b6d69a882be.jpg")
    await bot.send_photo(message.chat.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNh5h68CGoCiFOdg3XawGky8vBOzz2gjN9gg&usqp=CAU")

#send audio
@app.on_message(filters.audio & filters.private)
async def audio(bot, message):
    await message.reply_text(message.audio.file_id) #get the audio link

@app.on_message(filters.command('audio'))
async def command6(bot, message):
    await bot.send_audio(message.chat.id, "CQACAgUAAxkBAAPIZe24rC1Y6LJR_DaspVpGygPf0ekAAtMOAALepmhXQq-80lFCZYEeBA") #send the audio file

#send document
@app.on_message(filters.document & filters.private)
async def document(bot, message):
    await message.reply_text(message.document.file_id) #get the document id

@app.on_message(filters.command('file'))
async def command7(bot, message):
    await bot.send_document(message.chat.id, "BQACAgUAAxkBAAIBAWXtxPKFhdtS85bJ0Qa70XNsOUanAAImDwAC3qZoVxJY32wB-KacHgQ")

#send sticker
@app.on_message(filters.sticker & filters.private)
async def sticker(bot, message):
    await message.reply_text(message.sticker.file_id) #get the sticker id

@app.on_message(filters.command('sticker'))
async def command8(bot, message):
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIBBWXtxjvvm6S4Hok9JWppe5F0Q2vSAAIQAQACUomRI8RI8frMHAbzHgQ")

#send video
@app.on_message(filters.video & filters.private)
async def video(bot, message):
    await message.reply_text(message.video.file_id) #get the video id

@app.on_message(filters.command('video'))
async def command9(bot, message):
    await bot.send_video(message.chat.id, "BAACAgEAAxkBAAIBCmXtx5sg15yUv8UWzcGlu6Lu9UiSAAKPAAMFrylFvSJs7TptjcMeBA") 

# send voice
@app.on_message(filters.voice & filters.private)
async def voice(bot, message):
    await message.reply_text(message.voice.file_id) #get the voice id

@app.on_message(filters.command('voice'))
async def command9(bot, message):
    await bot.send_voice(message.chat.id, "CgACAgQAAxkBAAIBHWXtySQ3jSvgHVRp4M1mhJ5E_s8RAAKcBAACkDKkUZ9RIf9wIzrdHgQ")

@app.on_message(filters.text)
async def delete (bot, message):
    word_list = ["Promotion"]
    if message.text in word_list:
        await bot.delete_messages(message.chat.id, message.message_id)
        await bot.send_message(message.chat.id, "Blocklisted Word")
        return
@app.on_message(filters.command('bot_version'), group=69)
async def version (bot, message):
    await bot.send_message(message.chat.id, "Bot Version ~ 1.1")

if __name__ == '__main__':
    try:
        loop.run_until_complete(main())
    except:
        pass
