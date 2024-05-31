import math

from pyrogram.types import InlineKeyboardButton

from LippsMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "ʜᴇʟʟᴏ 🙋‍♂️"
    elif 10 < umm < 20:
        bar = "ɪ ᴀᴍ ʜᴜɴɢᴀᴍᴀ ᴍᴜsɪᴄ ʙᴏᴛ ❤"
    elif 20 <= umm < 30:
        bar = "ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❤"
    elif 30 <= umm < 40:
        bar = "ɪ ᴍ ʜᴇʀᴇ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ ʟᴀɢ ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ"
    elif 40 <= umm < 50:
        bar = "ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ"
    elif 50 <= umm < 60:
        bar = "ғᴏʀ ᴀɴʏ ǫᴜᴇʀʏ"
    elif 60 <= umm < 70:
        bar = "ᴊᴏɪɴ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴏʀ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴍʏ ᴅᴇᴠ."
    elif 70 <= umm < 80:
        bar = "ᴇɴᴊᴏʏ ʟᴀɢғʀᴇᴇ ᴍᴜsɪᴄ ᴡɪᴛʜ ʜᴜɴɢᴀᴍᴀ ᴍᴜsɪᴄ ❤"
    elif 80 <= umm < 95:
        bar = "🌸🌸🌸🌸"
    else:
        bar = "ᴛʜᴀɴᴋ ʏᴏᴜ ❤"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="💥 ᴊᴏɪɴ Ɦᴇʀᴇ & sᴜᴘᴘᴏʀᴛ 💞",url=f"https://t.me/infinitelovefeelboyxd"),
            InlineKeyboardButton(text="🥀 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ  💞",url=f"https://t.me/Stylish_Bio_Dp_0"),
            InlineKeyboardButton(text="❤ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❤",url=f"https://t.me/niksonfire"),
            InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀",url=f"https://t.me/feel_boy_1"),



        ],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"LippsPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"LippsPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
