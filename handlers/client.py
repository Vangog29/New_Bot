from telegram import Update
from telegram.ext import *
#from bot import updater
from keyboard.client import *
import keyboard.client
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
from bot import data_base
from apps.state import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Я бот. Что будем делать?", reply_markup=inline_kayboard,
    )


async def echo (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def translate_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text='Введите слово для перевода'
    )

    return translate(update=update, context=context)


async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Запуск перевода")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Введите слово для перевода и добавте команду /Translate",
    )

async def comm_trans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)
    DATA = {"source": text, "lang": "en-ru", "as": "raw"}
    resp = requests.post("https://fasttranslator.herokuapp.com/api/v1/text/to/text", data=DATA)
    out_text = resp.text
    print(out_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=out_text)


async def menu (update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'trans':
        return await translate(update=update, context=context)
    elif query.data == 'yes_reg':
        return await reg_in_db(update=update, context=context)

async def registration (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Хотите зарегистрироваться?", reply_markup=reg_yes_no_kayboard,
    )

async def reg_in_db(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if data_base.check_user(update.effective_user.id) is False:
        data_base.add_user(update.effective_user.id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Вы добавлены в базу")
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Вы уже зарегистрированы")

#-------------------------------------------------------------------


#------------------Registr handlers------------------

start_handler = CommandHandler('start', start)
registration_handler = CommandHandler('registration', registration)
#echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
caps_handler = CommandHandler('caps', caps)
translate_handler = MessageHandler(filters.Text('Перевод')& (~filters.COMMAND), translate_button)
menu_handler = CallbackQueryHandler(menu)
comm_trans_handler = CommandHandler('Translate', comm_trans)


