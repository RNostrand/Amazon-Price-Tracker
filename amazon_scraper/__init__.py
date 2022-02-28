from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from amazon_scraper.config import Config

db = SQLAlchemy()

bcrypt = Bcrypt()

mail = Mail()

login_manager= LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from amazon_scraper.users.routes import users
    from amazon_scraper.products.routes import products
    from amazon_scraper.main.routes import main
    from amazon_scraper.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(products)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app