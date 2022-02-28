import requests 
from bs4 import BeautifulSoup
import time
from itertools import cycle
import traceback
import random
from amazon_scraper.functions.headers import get_headers_list
from flask import current_app

def extractSearch(query, page=1):
    headers_list = get_headers_list()

    url = f'https://www.amazon.com/s?k={query}&page={page}'
    headers = random.choice(headers_list)
    
    soup = None
    while True:
        try:
            time.sleep(1.1)
            proxy = current_app.config['PROXY']
            res = requests.get(url, headers=headers, proxies={"http": proxy}, timeout=2.5)
            if "To discuss automated access to Amazon data please contact" in res.text:
                pass
                print('Error: Blocked')
            else:
                soup = BeautifulSoup(res.content, 'lxml')
                break
        except:
            pass
            print('Connection Error')
        if soup != None:
            break
    return soup

def transformSearch(soup):
    items = []
    products = soup.find_all('div', class_="s-asin") #data-component-type=s-search-result
    for item in products:
        asin = item.get("data-asin"),
        
        try: 
            name = item.find('span', class_ = "a-text-normal").text.strip(),
        except:
            name = 'Name Unavailable',

        try: 
            image = item.find('img').get('src'),
        except:
            image = 'Image Unavailable',

        try: 
            price = item.find('span', class_ = "a-offscreen").text.strip(),
        except:
            price = 'Price Unavailable',

        try: 
            stars = item.find('span', class_ = "a-icon-alt").text.strip(),
        except:
            stars = 'Stars Unavailable'

        try: 
            ratings = item.find('span', class_ = "a-size-base s-underline-text").text.strip(),
        except:
            ratings = 'Reviews Unavailable'

        #find returns tuple, convert to string
        asin = asin[0] 
        name= name[0] 
        image = image[0]
        price = price[0]
        stars = stars[0]
        ratings = ratings[0]

        item = {
            'asin': asin,
            'name': name,
            'image': image,
            'price': price,
            'stars': stars,
            'ratings': ratings,
        }
        items.append(item)
    return items
    
