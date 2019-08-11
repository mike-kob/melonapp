from sqlalchemy import func
from models import db


class Number(db.Model):
    __tablename__ = "numbers"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20))

    created = db.Column(db.DateTime(), server_default=func.now())
