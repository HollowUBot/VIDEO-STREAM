# Copyright (C) 2021-2022 By @piovendoti

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Benvenuto [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ti permette di riprodurre musica e video sui gruppi attraverso le nuove chat video di Telegram!**

💡 **Scopri tutti i comandi del Bot e come funzionano cliccando sul pulsante » 📚 Comandi!**

🔖 **Per sapere come utilizzare questo bot, fare clic su » ❓ Pulsante Guida di base!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Aggiungimi al tuo gruppo ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Guida di base", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Comandi", callback_data="cbcmds"),                    
                ],
                [
                    InlineKeyboardButton(
                        "👥 Gruppo ufficiale", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Canale ufficiale", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),                    
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **Per prima cosa, aggiungimi al tuo gruppo.**
2.) **Quindi promuovimi come amministratore e concedi tutte le autorizzazioni tranne Amministratore anonimo.**
3.) **Dopo avermi promosso, digita /reload nel gruppo per aggiornare i dati dell'amministratore.**
3.) **Aggiungi @{ASSISTANT_NAME} al tuo gruppo o digita /userbotjoin per invitarlo.**
4.) **Attiva la chat video prima di iniziare a riprodurre video/musica.**
5.) **A volte, ricaricare il bot utilizzando il comando /reload può aiutarti a risolvere alcuni problemi.**

⚡ __Creato da: @piovendoti__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Torna indietro", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Ciao [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Creato da: @piovendoti__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Comandi admin", callback_data="cbadmin"),                    
                ],[
                    InlineKeyboardButton("📚 Comandi base", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Indietro", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Ecco i comandi di base:

» /mplay (nome/collegamento del brano) - riprodurre musica in chat video
» /vplay (nome/collegamento del video) - riprodurre video su chat video
» /vstream - riproduci video dal vivo da YouTube
» /playlist - mostrare la playlist
» /video (query) - scarica video da youtube
» /song (query) - scarica la canzone da youtube
» /lyric (query) - elimina il testo della canzone
» /search (query) - cerca un collegamento video di YouTube

» /ping - mostra lo stato del ping del bot
» /uptime - mostra lo stato di attività del bot
» /alive - mostra le informazioni sul bot (nel gruppo)

⚡️ __Creato da: @piovendoti__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Ecco i comandi dell'amministratore:

» /pause - mettere in pausa il brano
» /resume - riprendere il brano
» /skip - passa al brano successivo
» /stop - fermare il brano
» /vmute - disattivare l'audio dell'userbot nella chat vocale
» /vunmute - riattiva l'userbot nella chat vocale
» /volume `1-200` - regolare il volume della musica (l'userbot deve essere amministratore)
» /reload - ricarica il bot e aggiorna i dati dell'amministratore
» /userbotjoin - invita l'userbot a unirsi al gruppo
» /userbotleave - ordina all'userbot di uscire dal gruppo

⚡️ __Creato da: @piovendoti__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **impostazioni di** {query.message.chat.title}\n\n⏸ : mettere in pausa il brano\n▶️ : avviare il brano\n🔇 : muta il bot\n🔊 : smuta il bot\n⏹ : ferma il bot",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Chiudi", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ Nessuno è attualmente nella chat vocale", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Solo l'amministratore con l'autorizzazione per la gestione delle chat vocali può toccare questo pulsante !", show_alert=True)
    await query.message.delete()
