from typing import Optional

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import bot
from settings import CHANNEL_NAME


def send_to_channel(number_id: int) -> Optional[Message]:
    button_list = [
        [InlineKeyboardButton("Dare!", callback_data=number_id)],
    ]
    reply_markup = InlineKeyboardMarkup(button_list)
    msg = bot.send_message(chat_id=CHANNEL_NAME,
                           text="Hey, here's new customer struggling to have his belly full "
                                "of melons. Who's gonna dare to satisfy his appetites?\n\n"
                                "But remember, that you have to start chatting with this "
                                "wonderful <a href=\"https://t.me/Regsmthbot\">bot</a> ",
                           reply_markup=reply_markup,
                           parse_mode='HTML')
    return msg
