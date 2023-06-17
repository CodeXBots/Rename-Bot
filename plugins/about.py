import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"᚛› 𝐔𝐬𝐞𝐫𝐬 - {total_user()}\n᚛› 𝐑𝐞𝐧𝐚𝐦𝐞 𝐅𝐢𝐥𝐞𝐬 - {total_rename}\n᚛› 𝐑𝐞𝐧𝐚𝐦𝐞𝐝 𝐒𝐢𝐳𝐞 - {humanbytes(int(total_size))}",quote=True)
