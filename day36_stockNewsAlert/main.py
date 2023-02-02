import requests
import password
from datetime import datetime, timedelta, date
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 3.5% between yesterday and the day before yesterday then print("Get News").
alpha_parameters = {"function":"TIME_SERIES_DAILY_ADJUSTED", "symbol": STOCK, "apikey": password.alpha_key}
alpha_response = requests.get(url = "https://www.alphavantage.co/query", params = alpha_parameters)
alpha_response.raise_for_status()
data = alpha_response.json()
ts_data = data["Time Series (Daily)"]

today = datetime.now()
yesterday = str((today - timedelta(days = 1)).date())
before_yesterday = str((today - timedelta(days = 2)).date())

yesterday_close = float(ts_data[yesterday]["4. close"])
before_yesterday_close = float(ts_data[before_yesterday]["4. close"])

delta = (yesterday_close / before_yesterday_close) - 1


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_parameters ={"q": COMPANY_NAME, "from": before_yesterday, "sortBy": "publishedAt", "apiKey": password.news_key, "language": "en"}

if abs(delta) >= .035:
    news_response = requests.get(url = "https://newsapi.org/v2/everything", params = news_parameters)
    news_response.raise_for_status()
    news = news_response.json()
    news_3 = news["articles"][0:3]
    # interested in title, description and url keys
    news_text = [article["title"]+"\n"+article["description"]+"\n"+article["url"] for article in news_3]

## STEP 3: Use https://telegram.org
    # send each one of these to telegram bot
    for article in news_text:
        parameters_telegram = {"chat_id": password.chat_id, "text": article}
        send_message = requests.get(url = "https://api.telegram.org/bot"+password.bot_token+"/sendMessage", params = parameters_telegram)

        send_message.raise_for_status()

        send_message.json()

