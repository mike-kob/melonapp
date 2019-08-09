from flask import Flask, render_template, request, Response

from settings import RUN_ENV

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/phone_number/', methods=['POST'])
def phone_number():
    return Response(status=200)


if RUN_ENV == 'DEV':
    app.run()
