#Telegram bot home work 5886021512:AAFI67WYPN9MNSEBYJoPa3ridl7GhDZLyAQ

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from log import log

def hello(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5886021512:AAFI67WYPN9MNSEBYJoPa3ridl7GhDZLyAQ')

updater.dispatcher.add_handler(CommandHandler("hello", hello))




print("bot is run")

updater.start_polling()
updater.idle()