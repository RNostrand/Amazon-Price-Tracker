from os import environ
from dotenv import load_dotenv


class Config:
    load_dotenv()

    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get("EMAIL_USER")
    MAIL_PASSWORD = environ.get("EMAIL_PASS")
    PROXY = environ.get("PROXY")
