from telegram import Bot, Update

from models.models import Number
from settings import CHANNEL_NAME


def callback_handler(bot: Bot, update: Update) -> None:
    user_id = update.callback_query.from_user.id
    num_id = update.callback_query.data
    from app import app

    with app.app_context():
        number = Number.query.get(num_id)
    msg_sent = None
    if number is not None:
        msg_sent = bot.send_message(chat_id=user_id,
                                    text='Ok ok, I see that you want to deliver some '
                                         'fresh juicy melon. I can feel your impatience! '
                                         'So, here\'s your client:\n'f'<b>{number.number}</b>',
                                    parse_mode='HTML')

    if msg_sent:
        message_id = update.callback_query.message.message_id
        bot.delete_message(CHANNEL_NAME, message_id)


def message_handler(bot: Bot, update: Update) -> None:
    user_id = update.message.chat_id
    if update.message.text == '/start':
        bot.send_message(chat_id=user_id,
                         text='Hello my dearest friend. I hope you will enjoy '
                              'your melon delivery craft.\n I\'m '
                              'not a talkative bot, you know. Everything you need '
                         f'you can find here: {CHANNEL_NAME}')
    else:
        bot.send_message(chat_id=user_id,
                         text='Hey you, I think I said I don\'t want to talk.\n'
                         f'{CHANNEL_NAME}')
