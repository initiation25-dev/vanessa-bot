from telegram.ext import Updater, CommandHandler

TOKEN = "7882970117:AAFcNyNeEMiFNYhQh0LamJMwA2sG3sga8vU"  # remplace par TON token si t'en as un nouveau

def start(update, context):
    update.message.reply_text("Hey trésor, Vanessa est en ligne ! 😏")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
