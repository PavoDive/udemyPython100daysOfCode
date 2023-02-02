from password import api_key, bot_token, chat_id
import requests
# import os

# chat_id = os.environ.get("CHAT_ID") # from environ variable
MY_LAT = 3.2579283267853185
MY_LONG = -76.57078066276841

parameters = {"appid":api_key, "lat": MY_LAT, "lon": MY_LONG, "units": "metric", "exclude": "current,minutely,daily,alerts"}

# original version of the lecture was 3.0, but it is now (2023-02-01) behind a paywall. 2.8 worked.
response = requests.get(url = "https://api.openweathermap.org/data/2.8/onecall", params = parameters)
response.raise_for_status()

data = response.json()
hourly_data_12h = data["hourly"][0:11]
# id < 700 means light rain --> snow, so needs umbrella!
conditions_12h = [hour["weather"][0]["id"] for hour in hourly_data_12h]
bring_an_umbrella = any([id < 700 for id in conditions_12h])

    
# ------------------- send telegram message ----
# https://core.telegram.org/bots/api#sendmessage
# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

if bring_an_umbrella:
    parameters_telegram = {"chat_id": chat_id, "text": "bring an umbrella."}
    send_message = requests.get(url = "https://api.telegram.org/bot"+bot_token+"/sendMessage", params = parameters_telegram)

    send_message.raise_for_status()

    send_message.json()

# --------- environment variables -----------
# It is possible to save variables to local environment, to avoid
# uploading code with API keys or passwords.
# The way to do it is **in the console**:
#
# export TEST=this/is/a/test
#
# and then in the code use:
#
# value_of_test = os.environ.get("TEST")
#
# environment variables can be deleted by
# unset TEST

# ----------------- More APIs -------------
# apilist.fun
# https://site.financialmodelingprep.com/developer/docs/
