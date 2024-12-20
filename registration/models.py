from main.settings import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"id: {self.id}"