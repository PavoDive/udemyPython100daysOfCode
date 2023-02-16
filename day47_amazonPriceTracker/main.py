from amazonPrice import AmazonPrice
from telegram import Telegram
import time

url = "https://www.amazon.com/Secura-60-Minute-Mechanical-Countdown-Collapsible/dp/B0895S4NWP"

item = AmazonPrice(url)
t = Telegram()

threshold_price = 47.50

while True:
    if item.price <= threshold_price:
        print("Sending message to Telegram Bot")
        t.send_message(f"The price of your tracked item is at ${item.price}!\nBuy it at {url}")
        break
    else:
        print("Sorry, the current price is above the threshold. Waiting 3 hours before querying it again.")
        time.sleep(60*60*3) # 3 hours before checking again.
        item.update_price()








