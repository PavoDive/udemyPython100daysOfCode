import requests
import password
import datetime

class Sheety:
    def __init__(self):
        """

        """
        self.headers = {"Authorization": password.sheety_token}
        self.url = "https://api.sheety.co/5d3eed5e35cde1309ff5d6bc8e52ec6e/myWorkouts/workouts"


    def post_food(self, foods):
        now_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        now_time = datetime.datetime.now().time().strftime("%H:%M:%S")
        for food in foods:
            body = {"workout": {"date": now_date, "time": now_time, "exercise": food["food_name"], "duration": 0, "calories": food["nf_calories"], "cholesterol": food["nf_cholesterol"]}}
            failure = 1
            count = 1
            while failure != None and count < 1000:
                write_row = requests.post(url = self.url, headers = self.headers, json = body)
                failure = write_row.raise_for_status()
                count += 1


    def post_exercise(self, exercises):
        now_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        now_time = datetime.datetime.now().time().strftime("%H:%M:%S")
        for exercise in exercises:
            body = {"workout":{"date": now_date, "time": now_time, "exercise": exercise["name"], "duration": exercise["duration_min"], "calories": -exercise["nf_calories"], "cholesterol": 0}}
            failure = 1
            count = 1
            while failure != None and count < 1000:
                write_row = requests.post(url = self.url, headers = self.headers, json = body)
                failure = write_row.raise_for_status()
                count += 1

        

# ----------------- this is the way of reading the rows -----------------

# worksheet = requests.get(url = get_url, headers = sheety_headers)
# worksheet.raise_for_status()
# data = worksheet.json()["workouts"]
# df_data = pandas.DataFrame.from_dict(data)


