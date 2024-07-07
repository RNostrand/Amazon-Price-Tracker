from amazon_scraper import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(125), nullable=False)

    products = db.relationship("Product", backref="author", lazy=True)

    def get_reset_token(self, expires_sec=15000):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.email}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)
    name = db.Column(db.Text(), nullable=False)
    price = db.Column(db.String(), nullable=False)
    stars = db.Column(db.String(), nullable=False)
    ratings = db.Column(db.String(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.price}', '{self.stars}', '{self.ratings}')"
