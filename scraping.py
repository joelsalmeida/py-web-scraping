from urllib import response
import requests
from parsel import Selector

site_main_url = "http://books.toscrape.com/"
main_response = requests.get(site_main_url)
selector = Selector(text=main_response.text)

titles = selector.css(".product_pod h3 a::attr(title)").getall()
print(titles)

prices = selector.css(".product_price .price_color::text").getall()
print(prices)

for product in selector.css(".product_pod"):
    product_title = product.css("h3 a::attr(title)").get()
    product_price = product.css(".price_color::text").get()
    print(product_title, product_price)


BASE_URL = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'

while next_page_url:
    page_response = requests.get(BASE_URL + next_page_url)
    selector = Selector(text=page_response.text)

    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").get()
        print(title, price)

    next_page_url = selector.css(".next a::attr(href)").get()
