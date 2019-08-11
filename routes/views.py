from flask import render_template, request, Response, jsonify

from bot import manage_update
from bot.actions import send_to_channel
from models import db
from models.models import Number


def index():
    return render_template("index.html")


def phone_number():
    if request.is_json:
        str_num = request.json["p_num"]
        num_obj = Number(number=str_num)
        db.session.add(num_obj)
        db.session.commit()
        send_to_channel(num_obj.id)
        return jsonify({})
    else:
        return jsonify({})


def bot_webhook():
    manage_update(request.get_json(force=True))
    return Response('ok', 200)
