from flask import Flask

from settings import RUN_ENV

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__' and RUN_ENV == 'DEV':
    app.run()
