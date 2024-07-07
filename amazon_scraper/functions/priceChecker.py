import time

import schedule
from amazon_scraper import db, mail
from amazon_scraper.functions.product import extractProduct, getProductPrice
from amazon_scraper.models import Product, User
from flask_mail import Message


def sendEmail(product, price):
    msg = Message(
        "Price change found!",
        sender="noreply@demo.com",
        recipients=[product.author.email],
    )
    msg.body = f"""There has been a price change for a product you are tracking:
{product.name}:
The price has changed from {product.price} to {price}.
"""
    mail.send(msg)


def checkPrice():
    products = Products.query.all()
    for product in products:
        soup = extractProduct(product.asin)
        price = getProductPrice(soup)
        if price != product.price:
            sendEmail(product, price)


def scheduleChecker(func):
    schedule.every(24).hours.do(func)
    while True:
        schedule.run_pending()
        time.sleep(1)
