from telegram import Bot, Update
from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters

from settings import BOT_TOKEN


def callback_handler(bot: Bot, update: Update) -> None:
    user_id = update.callback_query.message.chat_id
    bot.send_message(user_id, 'Bla Bla')


def message_handler(bot: Bot, update: Update) -> None:
    user_id = update.message.chat_id
    bot.send_message(user_id, 'Bla Bla')


def start_bot_polling():
    # Set up the Updater
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CallbackQueryHandler(callback_handler))
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
