from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime


def log(update: Update, context: CallbackContext):
    file = open('log.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {datetime.datetime.now().time()},{update.message.text}\n')
    file.close()