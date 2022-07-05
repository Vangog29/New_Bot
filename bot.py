from telegram import Update
from  telegram.ext import CallbackContext, Updater, ApplicationBuilder

bot = ApplicationBuilder().token('5539375464:AAFLIZ4lI_EAumbqKi9c-2ldBhpcoI4KxXE').build()

#updater = Updater(
#        token='5539375464:AAFLIZ4lI_EAumbqKi9c-2ldBhpcoI4KxXE', #убрать токен в переменную окружения
#        use_context=True
#    )