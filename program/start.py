from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("Settimana", 60 * 60 * 24 * 7),
    ("Giorno", 60 * 60 * 24),
    ("Ore", 60 * 60),
    ("Min", 60),
    ("Sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **👋🏻 Benvenut@ {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Consente di riprodurre musica e video su gruppi attraverso le nuove video chat di Telegram!**

💡 **Scopri tutti i comandi del Bot e come funzionano cliccando sul pulsante » 📚 Comandi Bot!**

🔖 **Per sapere come utilizzare questo bot, si prega di fare clic su » ❓ Comandi di base (Guida)!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜️ Aggiungimi al tuo gruppo ⚜️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Guida di base", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Comandi", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ Dona", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Gruppo ufficiale", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Canale ufficiale", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🔰 Bot in fase di Aggiornamento! 🔰"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["infob", f"infob@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Gruppo", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Canale", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**👋🏻 Ciao {message.from_user.mention()}, io sono {BOT_NAME}**\n\n✨ Il bot funziona normalmente\n🍀 Sviluppatore: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Versione: `v{__version__}`\n✨ Stato di attività: `{uptime}`\n\n**Grazie per avermi aggiunto qui, per riprodurre video e musica sul tuo gruppo in chat video** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ping...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Stato del bot:\n"
        f"• **Tempo di attività:** `{uptime}`\n"
        f"• **Ora di inizio:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **Grazie per avermi aggiunto al gruppo !**\n\n"
                "**Promuovimi come amministratore del Gruppo, altrimenti non sarò in grado di funzionare correttamente, non dimenticarti di fare /invita per invitare il mio assistente.**\n\n"
                "**Una volta terminato, digita** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📣 Canale", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("💭 Supporto", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("👤 Assistante", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
