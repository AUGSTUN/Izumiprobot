from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os,re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from AnyaSuperBot import telethn as bot
from AnyaSuperBot import telethn as tgbot
from AnyaSuperBot.events import register
from AnyaSuperBot import dispatcher


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/d9c46e3db8952c020256b.jpg"
file2 = "https://telegra.ph/file/9e9e1112a16894e7998cf.jpg"
file3 = "https://telegra.ph/file/060b79fec4a50f48d59ba.jpg"
file4 = "https://telegra.ph/file/060b79fec4a50f48d59ba.jpg"
file5 = "https://telegra.ph/file/e2034322c680ed63a0c4f.jpg"
""" =======================CONSTANTS====================== """

@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("Click Here",data="information")]]
    on = await bot.send_file(event.chat_id, file=file2,caption= f"剣 Hey There, I'm Anya Forger 剣\n剣 I'm Created By [Xelcius](tg://user?id=5132611794)\n剣 Click The Button Below To Get Your Info", buttons=button)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    Saber = "YOUR DETAILS BY Saber 剣 \n\n"
    Saber += f"FIRST NAME : {PRO.first_name} \n"
    Saber += f"LAST NAME : {PRO.last_name}\n"
    Saber += f"YOU BOT : {PRO.bot} \n"
    Saber += f"RESTRICTED : {PRO.restricted} \n"
    Saber += f"USER ID : {boy}\n"
    Saber += f"USERNAME : {PRO.username}\n"
    await event.answer(Saber, alert=True)
  except Exception as e:
    await event.reply(f"{e}")

__help__ = """
/myinfo: shows your info in inline button
"""

__mod_name__ = "MyInfo"
__command_list__ = [
    "MyInfo"
]
