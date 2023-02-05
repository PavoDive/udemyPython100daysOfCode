import requests
import password
import datetime

class Sheety:
    def __init__(self):
        """

        """
        self.__headers = {"Authorization": password.sheety_token}
        self.__endpoint = f"https://api.sheety.co/{password.sheety_user_string}"
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
        url = f"{self.__endpoint}/flightDeals/prices"
        worksheet = requests.get(url = url, headers = self.__headers)
        worksheet.raise_for_status()
        return worksheet.json()["prices"]
        

    def __user_validation(self):
        first_name = input("Please input your first name: ").title()
        last_name = input("Please input your last name: ").title()
        email = input("Please input your email: ").lower()
        email2 = input("Please retype your email: ").lower()
        if email != email2:
            raise Exception("Emails do not match. Try again.")
        else:
            return (first_name, last_name, email)
        
    
    def write_user_data(self):
        url = f"{self.__endpoint}/flightDeals/users"

        user_data = self.__user_validation()
        body = {"user": {"firstName": user_data[0],
                         "lastName": user_data[1],
                         "email": user_data[2]
                         }
                }
        failure = 1
        count = 1
        while failure != None and count < 1000:
            write_row = requests.post(url = url,
                                      headers = self.__headers,
                                      json = body)
            failure = write_row.raise_for_status()
            count += 1
        print(f"\nWelcome to the flight deals club, {user_data[0]}!\n")

    def get_user_destination(self):
        url = f"{self.__endpoint}/flightDeals/prices"
        city = input("Type the name of a city you'd like to travel to: ").title()
        try:
            top_price = int(input("Type the price under which you'd like us to email offers for that destination (numbers only in USD): "))
        except ValueError:
            print("Only integer numbers are allowed!")
        else:
            body = {"price": {"destination": city,
                              "cutoffPrice": top_price,
                             }
                    }
            failure = 1
            count = 1
            while failure != None and count < 1000:
                write_row = requests.post(url = url,
                                          headers = self.__headers,
                                          json = body)
                failure = write_row.raise_for_status()
                count += 1
            print(f"\nYour city-top price combination was added successfully!")
            
        

    def read_user_data(self):
        url = f"{self.__endpoint}/flightDeals/users"
        worksheet = requests.get(url = url, headers = self.__headers)
        worksheet.raise_for_status()
        return worksheet.json()["users"]
        
