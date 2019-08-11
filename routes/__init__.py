from bot import start_bot_polling
from settings import RUN_ENV
from routes.views import index, phone_number, bot_webhook
from settings import BOT_TOKEN


def init_app(app):
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/api/phone_number/', view_func=phone_number, methods=['POST'])

    if RUN_ENV == 'PROD':
        app.add_url_rule(f'/{BOT_TOKEN}', view_func=bot_webhook, methods=['POST'])
    elif RUN_ENV == 'DEV':
        start_bot_polling()
