from pyrogram.types import Message
from pyrogram import filters
from AnyaSuperBot import pbot
from AnyaSuperBot.utils.errors import capture_err
from AnyaSuperBot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text to generate carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text to generate carbon.`")
    m = await message.reply_text("`Generating Carbon...`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading Carbon...`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()

__mod_name__ = "Carbon"

__help__ = """

Making carbon of a centain text.

❍ /carbon *:* Makes carbon of replied text.

 """
