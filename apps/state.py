from telegram import *
from telegram.ext import *
from keyboard.client import *
import keyboard.client
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from apps.db import *


WORD, TRANS = range(2)



async def start_dict(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:


    await update.message.reply_text(
        "Вы хотите добавить новые слова в свой личный словарь? "
        "Введите /cancel что бы прервать процесс.\n\n"
        "Введите слово на английском",
        )

    return WORD

async def word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    context.user_data['word'] = str(update.message.text)
    await update.message.reply_text("Спасибо. Теперь введите перевод")

    return TRANS

async def trans(update: Update, context: ContextTypes.DEFAULT_TYPE, data_base: data_base) -> int:
    context.user_data['trans'] = str(update.message.text)

    await update.message.reply_text(
        "Спасибо. Вы ввели"
        )

    data_base.add_word(update.effective_user.id, context.user_data.get('word'), context.user_data.get('trans'))
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Ввод отменен"
        )

    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start_dict", start_dict)],
    states={
        WORD: [MessageHandler(filters.TEXT, word)],
        TRANS: [MessageHandler(filters.TEXT, trans)],
    },
        fallbacks=[CommandHandler("cancel", cancel)],
)