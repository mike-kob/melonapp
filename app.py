from flask import Flask, render_template, request, Response

from bot import start_bot_polling, message_handler, callback_handler
from settings import RUN_ENV, BOT_TOKEN
from telegram import Bot, Update

app = Flask(__name__)
bot = Bot(BOT_TOKEN)


def index():
    return render_template("index.html")


def phone_number():
    return Response(status=200)


def bot_webhook():
    try:
        update = Update.de_json(request.get_json(force=True), bot)
    except Exception as e:
        return Response(f"Not ok:{e}", status=500)
    if update.message:
        message_handler(bot, update)
    elif update.callback_query:
        callback_handler(bot, update)

    return Response('ok', 200)


app.add_url_rule('/', view_func=index)
app.add_url_rule('/api/phone_number/', view_func=phone_number, methods=['POST'])
if RUN_ENV == 'PROD':
    app.add_url_rule(f'/{BOT_TOKEN}', view_func=bot_webhook, methods=['POST'])
elif RUN_ENV == 'DEV':
    app.run()
    start_bot_polling()
