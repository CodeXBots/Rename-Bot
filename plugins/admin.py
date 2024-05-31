import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
ADMIN = int(os.environ.get("ADMIN", 1255023013))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔") 


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("Basic", callback_data="vip1")
				   ], [
					InlineKeyboardButton("Standard", callback_data="vip2")
				   ], [
					InlineKeyboardButton("Premium", callback_data="vip3")
					]]))
        			

@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"ᴅᴏ  ʏᴏᴜ  ʀᴇᴀʟʟʏ  ᴡᴀɴᴛ  ᴛᴏ  ʀᴇꜱᴇᴛ  ʜɪꜱ  ʟɪᴍɪᴛ.",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton(" 𝐘𝐞𝐬   ✅ ",callback_data = "dft")],
				   [InlineKeyboardButton(" 𝐍𝐨   ❌ ",callback_data = "cancel")]
				   ]))

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"Basic")
	addpre(int(user_id))
	await update.message.edit("ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ  ɪɴᴄʀᴇᴀꜱᴇᴅ  ᴛᴏ  10 ɢʙ  ᴘᴇʀ  ᴅᴀʏ.")
	await bot.send_message(user_id,"ʏᴏᴜ  ᴀʀᴇ  ᴜᴘɢʀᴀᴅᴇᴅ  ᴛᴏ  ʙᴀꜱɪᴄ  ᴘʟᴀɴ.")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 53687091200
	uploadlimit(int(user_id),53687091200)
	usertype(int(user_id),"Standard")
	addpre(int(user_id))
	await update.message.edit("ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ  ɪɴᴄʀᴇᴀꜱᴇᴅ  ᴛᴏ  50 ɢʙ  ᴘᴇʀ  ᴅᴀʏ.")
	await bot.send_message(user_id,"ʏᴏᴜ  ᴀʀᴇ  ᴜᴘɢʀᴀᴅᴇᴅ  ᴛᴏ  ꜱᴛᴀɴᴅᴀʀᴅ  ᴘʟᴀɴ.")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 107374182400
	uploadlimit(int(user_id), 107374182400)
	usertype(int(user_id),"Premium")
	addpre(int(user_id))
	await update.message.edit("ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ  ɪɴᴄʀᴇᴀꜱᴇᴅ  ᴛᴏ  100 ɢʙ  ᴘᴇʀ  ᴅᴀʏ.")
	await bot.send_message(user_id,"ʏᴏᴜ  ᴀʀᴇ  ᴜᴘɢʀᴀᴅᴇᴅ  ᴛᴏ  ᴘʀᴇᴍɪᴜᴍ  ᴘʟᴀɴ.")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 2147483648
	uploadlimit(int(user_id), 2147483648)
	usertype(int(user_id),"Free")
	addpre(int(user_id))
	await update.message.edit("ᴜꜱᴇʀ  ʟɪᴍɪᴛ  ʜᴀꜱ  ʙᴇᴇɴ  ʀᴇꜱᴇᴛ  ꜱᴜᴄᴄᴇꜱꜱꜱꜰᴜʟʟʏ.")
	await bot.send_message(user_id,"ʏᴏᴜʀ  ʟɪᴍɪᴛ  ʜᴀꜱ  ʙᴇᴇɴ  ʀᴇꜱᴇᴛ  ꜱᴜᴄᴄᴇꜱꜱꜱꜰᴜʟʟʏ.\n\nᴄᴏɴᴛᴀᴄᴛ  <a href='https://telegram.dog/CodeXBro'>**ᴏᴡɴᴇʀ**</a>  ꜰᴏʀ  ᴍᴏʀᴇ  ᴅᴇᴛᴀɪʟꜱ.")

