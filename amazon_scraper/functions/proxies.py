import requests
from lxml.html import fromstring

# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr'):
#         if i.xpath('.//td[7][contains(text(),"yes")]') and i.xpath('.//td[5][contains(text(),"elite proxy")]'):
#             # if i.xpath('.//td[3][contains(text(),"US")]') or i.xpath('.//td[3][contains(text(),"CA")]') or i.xpath('.//td[3][contains(text(),"MX")]'):
#             #i.xpath('.//td[6][contains(text(),"yes")]')
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     print(proxies)
#     return proxies


# this get put in function inheriting this

# while True:
#     #Get and rotate proxies
#     proxies = get_proxies()
#     proxy_pool = cycle(proxies)
#     for i in range(1, len(proxies) + 1):
#         try:
#             time.sleep(0.2)
#             proxy = next(proxy_pool)
#             res = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=2.5)
#             if "To discuss automated access to Amazon data please contact" in res.text:
#                 print('Error: Blocked')
#             else:
#                 soup = BeautifulSoup(res.content, 'lxml')
#                 break
#         except:
#             print('Connection Error', i)
#     if soup != None:
#         break
#     else:
#         print('round ~~')
