import asyncio
import datetime
from LippsMusic import app
from pyrogram import Client
from LippsMusic.utils.database import get_served_chats
from config import START_IMG_URL, LOGGER_ID, AUTO_GCAST_MSG, AUTO_GCAST
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else False

START_IMG_URLS = "https://graph.org/file/ffe71cc40348f849a078c.jpg"

MESSAGES = f"""💗       ˹@{app.username}˼ ♪       💗

😭 иσтнιиg ѕρєᴄιαℓ ᴊυѕт αиσтнєʀ мυѕιᴄ вσт ✅🔺

✨ ɴᴏ ᴅᴏᴡɴᴛɪᴍᴇs
😘 ɴᴏ ᴘʀᴏᴍᴏᴛɪᴏɴs 
🥀 ɴᴏ ʟᴀɢ ɪssᴜᴇs 
💻 ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.

‣ 𝖢𝗁𝖾𝖼𝗄 𝖲𝗍𝖺𝗍𝗎𝗌 𝖮𝖿 𝖳𝗁𝖾 𝖡𝗈𝗍'𝗌 𝖧𝖾𝗋𝖾
‣ 𝖵𝗂𝗌𝗂𝗍 @ThinkGrowMore 𝖥𝗈𝗋 𝖬𝗈𝗋𝖾.."""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("α∂∂ ιи уσυʀ ɢʀσυρ", url=f"https://t.me/KritikaMusicBot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

MESSAGE = f"""💗       ˹@{app.username}˼ ♪       💗

😭 иσтнιиg ѕρєᴄιαℓ ᴊυѕт αиσтнєʀ мυѕιᴄ вσт ✅🔺

✨ ɴᴏ ᴅᴏᴡɴᴛɪᴍᴇs
😘 ɴᴏ ᴘʀᴏᴍᴏᴛɪᴏɴs 
🥀 ɴᴏ ʟᴀɢ ɪssᴜᴇs 
💻 ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.

‣ 𝖢𝗁𝖾𝖼𝗄 𝖲𝗍𝖺𝗍𝗎𝗌 𝖮𝖿 𝖳𝗁𝖾 𝖡𝗈𝗍'𝗌 𝖧𝖾𝗋𝖾
‣ 𝖵𝗂𝗌𝗂𝗍 @ThinkGrowMore 𝖥𝗈𝗋 𝖬𝗈𝗋𝖾.."""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" α∂∂ ιи уσυʀ ɢʀσυρ ", url=f"https://t.me/KritikaMusicBot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URLS, caption=caption, reply_markup=BUTTONS)
                    await asyncio.sleep(20)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
