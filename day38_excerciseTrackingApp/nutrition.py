import requests
import password

class Exercise():
    def __init__(self):
        """

        """
        self.headers = {"x-app-id": password.nut_app_id,
                       "x-app-key": password.nut_app_key}
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.parameters = {}


    def set_parameters(self, q):
        self.parameters = {"query": q,
                                 "gender": "male",
                                 "weight_kg": 76,
                                 "height_cm": 174,
                                 "age": 49
                                }        


    def query_exercise(self, q):
        self.set_parameters(q)
        count = 1
        failure = 1
        while failure != None and count < 100:
            exercise_response = requests.post(url = self.endpoint,
                                              headers = self.headers,
                                              json = self.parameters)
            failure = exercise_response.raise_for_status()
            count += 1
        return exercise_response.json()["exercises"]
        

class Nutrients():
    def __init__(self):
        """

        """
        self.headers = {"x-app-id": password.nut_app_id,
                       "x-app-key": password.nut_app_key}
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
        self.parameters = {}


    def set_parameters(self, q):
        self.parameters = {"query": q}   


    def query_food(self, q):
        self.set_parameters(q)
        count = 1
        failure = 1
        while failure != None and count < 100:
            food_response = requests.post(url = self.endpoint,
                                              headers = self.headers,
                                              json = self.parameters)
            failure = food_response.raise_for_status()
            count += 1
        return food_response.json()["foods"]
    
