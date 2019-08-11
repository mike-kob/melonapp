from flask import Flask
import bot
import models
import routes

from settings import DATABASE_URI


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

models.init_app(app)
routes.init_app(app)
bot.init_app(app)

if __name__ == '__main__':
    app.run()
