#Owned By @TheKaizuryu & @Xelcius

from telethon import events, Button, custom
import re, os
from AnyaSuperBot.events import register
from AnyaSuperBot import telethn as tbot
from AnyaSuperBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/d9c46e3db8952c020256b.jpg"
@register(pattern=("/alive"))
async def awake(event):
  Saber = f"**剣 Hii {event.sender.first_name} I'm Saber Sword** \n\n"
  Saber += "**剣 I'm Property OF @AogiriNetwork**\n\n"
  Saber += "**剣 Anya Forger 剣: Sword Master Version **\n\n"
  Saber += "**剣 Creator:** [U N K N O W N](t.me/XTheAnonymous)\n\n"
  Saber += "**剣 python-Telegram-Bot: 13.11**\n\n"
  BUTTON = [[Button.url("Support", "https://t.me/NexusXSupport"), Button.url("Updates", "https://t.me/AogiriNetwork")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Saber,  buttons=BUTTON)
