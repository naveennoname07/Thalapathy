import psutil, shutil
from os import execvp,sys , execl
from pyrogram import Client , filters

@Client.on_message(filters.command("restart") & ~filters.private)
async def restart(_,message):
    await message.delete()
    await message.reply_text("⚰️")
    execl(executable, executable, "bot.py")
