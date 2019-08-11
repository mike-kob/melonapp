from telegram import Bot, Update
from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters
from bot.handlers import message_handler, callback_handler

from settings import BOT_TOKEN

bot = Bot(BOT_TOKEN)


def init_app(app):
    pass


def manage_update(raw_update: dict) -> None:
    update = Update.de_json(raw_update, bot)
    if update.message:
        message_handler(bot, update)
    elif update.callback_query:
        callback_handler(bot, update)


def start_bot_polling():
    # Set up the Updater
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CallbackQueryHandler(callback_handler))
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
