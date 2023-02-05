import requests
import password

class Telegram:
    def __init__(self):
        """

        """



    def send_message(self, message):
        parameters = {"chat_id": password.chat_id, "text": message}
        sm = requests.get(url = "https://api.telegram.org/bot"+password.bot_token+"/sendMessage", params = parameters)

        sm.raise_for_status()
        return sm.json()
