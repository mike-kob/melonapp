from flask import render_template, request, Response, jsonify

from bot import manage_update
from models import db
from models.models import Number


def index():
    return render_template("index.html")


def phone_number():
    if request.is_json:
        num = request.json["p_num"]
        db.session.add(Number(number=num))
        db.session.commit()
        return jsonify({})
    else:
        return jsonify({})


def bot_webhook():
    manage_update(request.get_json(force=True))
    return Response('ok', 200)
