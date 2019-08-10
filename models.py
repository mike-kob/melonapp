from app import db


class Number(db.Model):

    __tablename__ = "numbers"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20))
