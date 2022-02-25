from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Torna Indietro", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("❕ Chiudi", callback_data="cls")]]
)


@Client.on_message(command(["riavvia", f"riavvia@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ Bot **correttamente riavviato !**\n✅ **Lista Staff aggiornata!**"
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• Mᴇɴᴜ", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="• Cʟᴏsᴇ", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ niente è attualmente in riproduzione")
        elif op == 1:
            await m.reply("✅ __codice__ **è vuoto.**\n\n**• l'userbot è uscito dalla chat vocale**")
        elif op == 2:
            await m.reply("🗑️ **Cancellare il codice**\n\n**• l'userbot è uscito dalla chat vocale**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **Salta al brano successivo.**\n\n🏷 **Nome:** [{op[0]}]({op[1]})\n💭 **Chat:** `{chat_id}`\n💡 **Stato:** `Attivo`\n🎧 **Richiesto da:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **removed song from queue:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "ferma", f"ferma@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ L'userbot si è disconnesso dalla chat video.")
        except Exception as e:
            await m.reply(f"🚫 **errore:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nessuno è in streaming**")


@Client.on_message(
    command(["pausa", f"pausa@{BOT_USERNAME}", "vpausa"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **Traccia in pausa.**\n\n• **Per riprendere lo streaming, utilizzare il**\n» comando /riprendi."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **nothing in streaming**")


@Client.on_message(
    command(["riprendi", f"riprendi@{BOT_USERNAME}", "vriprendi"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **Traccia ripresa.**\n\n• **Per mettere in pausa lo streaming, utilizzare il**\n» comando /pausa."
            )
        except Exception as e:
            await m.reply(f"🚫 **errore:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nessuno è in streaming**")


@Client.on_message(
    command(["muta", f"muta@{BOT_USERNAME}", "vmuta"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **Userbot mutato.**\n\n• **Per smutare l'userbot, usa il**\n» comando /smuta"
            )
        except Exception as e:
            await m.reply(f"🚫 **errore:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nessuno è in streaming**")


@Client.on_message(
    command(["smuta", f"smuta@{BOT_USERNAME}", "vsmuta"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **Userbot smutato.**\n\n• **Per mutare l'userbot, usa il**\n» comando /muta."
            )
        except Exception as e:
            await m.reply(f"🚫 **errore:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nessuno è in streaming**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sei un amministratore anonimo!\n\n» Tornare all'account utente dai diritti di amministratore.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⚠️ Solo l'amministratore con l'autorizzazione per la gestione delle chat vocali può toccare questo pulsante!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ Lo streaming è stato sospeso", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **errore:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nessuno è attualmente in streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sei un amministratore anonimo!\n\n» tornare all'account utente dai diritti di amministratore.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Solo l'amministratore con l'autorizzazione per la gestione delle chat vocali può toccare questo pulsante!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ Lo streaming ha ripreso a funzionare", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **errore:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nessuno è attualmente in streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sei un amministratore anonimo !\n\n» tornare all'account utente dai diritti di amministratore.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Solo l'amministratore con l'autorizzazione per la gestione delle chat vocali può toccare questo pulsante !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **Questo streaming è terminato**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **errore:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nessuno è attualmente in streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sei un amministratore anonimo !\n\n» torna all'account utente da admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 solo l'amministratore con l'autorizzazione per la gestione delle chat vocali può toccare questo pulsante !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 userbot disattivato con successo", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **errore:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nessuno è attualmente in streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sei un amministratore anonimo !\n\n» tornare all'account utente dai diritti di amministratore.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Solo l'amministratore con l'autorizzazione per la gestione delle chat vocali può toccare questo pulsante !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 userbot riattivato con successo", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **errore:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nessuno è attualmente in streaming", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **volume impostato su** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **errore:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nessuno è in streaming**")
