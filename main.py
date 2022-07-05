from telegram import Update
from  telegram.ext import CallbackContext, Updater, MessageHandler, CommandHandler
from bot import bot
from handlers.client import start_handler, caps_handler, translate_handler, menu_handler, comm_trans_handler



def main():
    print('Start BOT')

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

