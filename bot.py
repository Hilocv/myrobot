# Created by PROZEE



# installs python-telegram-bot for you

import os

os.system("pip install python-telegram-bot")



from telegram.ext import Updater, CommandHandler

updater = Updater("5232913510:AAHfXFgZb6MSNx2Tn9QTo1B9VMxT1D_RBGs", use_context = True) 

#start function

def start(update, context):

  context.bot.sendMessage(chat_id   = chat_id ,text = "HI {update.message.user.first_name}")

startHandle = CommandHandler("start", start)

updater.dispatcher.add_handler(startHandle)

updater.start_polling( )

updater.idle( )
