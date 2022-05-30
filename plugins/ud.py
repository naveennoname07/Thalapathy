Import requests
from pyrogram import filters, Cilent
from pyrogram.types import Message
from pyrogram import Client as Alita

@Alita.on_message(filters.command("ud"))
async def ud(_, message: Message):
        text = message.text.split(None, 1)[1]
        results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
        reply_text = f'results: {text}\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        ud = await message.reply_text("finding.. define.")
        await ud.edit_text(reply_text)
