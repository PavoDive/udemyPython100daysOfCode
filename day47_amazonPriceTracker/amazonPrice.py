import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
           "Accept-Language": "en-US,en;q=0.5"}

class AmazonPrice:
    def __init__(self, url):
        """
        This class searches for the price of an amazon item at
        the given url.

        """
        self.url = url
        self.price = 0.0
        self.update_price()


    def update_price(self):
        response = requests.get(url = self.url, headers = headers)
        response.raise_for_status()
        sp = BeautifulSoup(response.text, "html.parser")
        price = sp.find(name = "span", class_ = "a-offscreen").string
        self.price = float(price.replace("$", ""))
        return self.price

