from telegram import Update
from apps.db import BotDB
from telegram.ext import CallbackContext, Updater, ApplicationBuilder

bot = ApplicationBuilder().token('5539375464:AAFLIZ4lI_EAumbqKi9c-2ldBhpcoI4KxXE').build()
data_base = BotDB()
