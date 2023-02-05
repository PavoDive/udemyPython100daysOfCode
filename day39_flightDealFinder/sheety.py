import requests
import password
import datetime

class Sheety:
    def __init__(self):
        """

        """

    # def post_food(self, foods):
    #     now_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    #     now_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    #     for food in foods:
    #         body = {"workout": {"date": now_date, "time": now_time, "exercise": food["food_name"], "duration": 0, "calories": food["nf_calories"], "cholesterol": food["nf_cholesterol"]}}
    #         failure = 1
    #         count = 1
    #         while failure != None and count < 1000:
    #             write_row = requests.post(url = self.url, headers = self.headers, json = body)
    #             failure = write_row.raise_for_status()
    #             count += 1


    # def post_exercise(self, exercises):
    #     now_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    #     now_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    #     for exercise in exercises:
    #         body = {"workout":{"date": now_date, "time": now_time, "exercise": exercise["name"], "duration": exercise["duration_min"], "calories": -exercise["nf_calories"], "cholesterol": 0}}
    #         failure = 1
    #         count = 1
    #         while failure != None and count < 1000:
    #             write_row = requests.post(url = self.url, headers = self.headers, json = body)
    #             failure = write_row.raise_for_status()
    #             count += 1

        

    # ----------------- this is the way of reading the rows -----------------

    def read_destinations(self):
        headers = {"Authorization": password.sheety_token}
        url = f"https://api.sheety.co/{password.sheety_user_string}/flightDeals/prices"

        worksheet = requests.get(url = url, headers = headers)
        worksheet.raise_for_status()
        return worksheet.json()["prices"]
        



