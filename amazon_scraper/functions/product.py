import random
import time
import traceback
from itertools import cycle

import requests
from amazon_scraper.functions.headers import get_headers_list
from bs4 import BeautifulSoup
from flask import current_app


def extractProduct(asin):
    headers_list = get_headers_list()

    url = f"https://www.amazon.com/dp/{asin}"
    headers = random.choice(headers_list)

    soup = None
    while True:
        try:
            time.sleep(1.1)
            proxy = current_app.config["PROXY"]
            res = requests.get(
                url, headers=headers, proxies={"http": proxy}, timeout=2.5
            )
            if "To discuss automated access to Amazon data please contact" in res.text:
                pass
                # print('Error: Blocked')
            else:
                soup = BeautifulSoup(res.content, "lxml")
                break
        except:
            pass
            # print('Connection Error')
        if soup != None:
            break
    return soup


def transformProduct(soup):
    try:
        asin = soup.find("div", id="averageCustomerReviews").get("data-asin")
    except:
        asin = soup.find("input", id="all-offers-display-params").get("data-asin")

    try:
        name = soup.find("span", id="productTitle").text.strip()
    except:
        name = "Name Unavailable"

    try:
        image = soup.find("img", id="landingImage").get("src")
    except:
        image = "Image Unavailable"

    try:
        price = soup.find("span", class_="a-offscreen").text.strip()
    except:
        price = "Price Unavailable"

    try:
        stars = (
            soup.find("div", id="averageCustomerReviews")
            .find("span", class_="a-icon-alt")
            .text.strip()
        )
    except:
        stars = "Stars Unavailable"

    try:
        ratings = (
            soup.find("div", id="averageCustomerReviews")
            .find("span", id="acrCustomerReviewText")
            .text.strip()
        )
    except:
        ratings = "Revies Unavailable"

    # find sometimes? returns tuple, convert to string
    # asin=asin[0]
    # name= name[0]
    # image = image[0]
    # price = price[0]
    # stars = stars[0]
    # ratings = ratings[0]

    product = {
        "asin": asin,
        "name": name,
        "image": image,
        "price": price,
        "stars": stars,
        "ratings": ratings,
    }

    return product


def getProductPrice(soup):
    price = soup.find("span", class_="a-offscreen").text.strip()
    return price
