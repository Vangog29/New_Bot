from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, CommandHandler
from bot import bot, data_base
from apps import db
from handlers.client import *
from apps.state import *



def main():
    print('Start BOT')
    data_base.setup()
    bot.add_handler(conv_handler)
    bot.add_handler(registration_handler)
    bot.add_handler(translate_handler)
    bot.add_handler(menu_handler)
    bot.add_handler(start_handler)
#    bot.add_handler(echo_handler)
    bot.add_handler(caps_handler)
    bot.add_handler(comm_trans_handler)
    bot.run_polling()


#    print('Start BOT')
#    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
#    updater.start_polling()
#    updater.idle()


if __name__ == '__main__':
    main()

