import requests
import password

# ----------------- searching flights -----------------
# from here: how to setup the search: https://tequila.kiwi.com/portal/docs/user_guides/booking_api__general_information_
# and https://tequila.kiwi.com/portal/docs/tequila_api/search_api

class Kiwi:
    def __init__(self):
        """

        """
        self.query = {"fly_from": "CLO", # two letter country code ok
              "curr": "USD",
              "flight_type": "round",
              "limit": 10,
              }


    def set_query(self, **kwargs):
        """
        Required args are: 'fly_to', 'date_from', 'date_to',
        'price_to', and EITHER pair of 'nights_in_dst_from'
        and 'nights_in_dst_to' OR 'return_from' and 'return_to'.
        Optional args: 'select_airlines'. Remember that dates are
        to be inputted as DD/MM/YYYY.
        """
        list_of_valid_args = ["fly_to", "date_from", "date_to",
                              "price_to", "nights_in_dst_from",
                              "nights_in_dst_to", "return_from",
                              "return_to", "select_airlines"]
        
        valid_arguments = all([key in list_of_valid_args for key in kwargs.keys()])
        pair_nights = sum([key in ["nights_in_dst_from", "nights_in_dst_to"] for key in kwargs.keys()])
        pair_return = sum([key in ["return_to", "return_from"] for key in kwargs.keys()])
        if not valid_arguments:
            raise Exception("Invalid argument name")
        if not (pair_nights, pair_return) in [(2, 0), (0, 2)]:
            raise Exception("EITHER pair of 'nights_in_dst_from' and 'nights_in_dst_to' OR 'return_from' and 'return_to' are required.")

        self.query.update(**kwargs)
                  

    def get_flights(self, **kwargs):
        """
        Required args are: 'fly_to', 'date_from', 'date_to',
        'price_to', and EITHER pair of 'nights_in_dst_from'
        and 'nights_in_dst_to' OR 'return_from' and 'return_to'.
        Optional args: 'select_airlines'. Remember that dates are
        to be inputted as DD/MM/YYYY.
        """
        headers = {"Content-Type": "application/json",
                        "apikey": password.kiwi_api_key,
                        "Content-Encoding": "gzip"}
        endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.set_query(**kwargs)
        # # try:
        #     whatever
        # # except typeoferror:
        #     actions
        # # except typeoferror as error_message:
        #     print(f"error msg: {error_message}")
        kr = requests.get(url = endpoint, headers = headers, params = self.query)
        try:
            kr.raise_for_status()
        except requests.exceptions.HTTPError as error_message:
            print("Error: {error_message}")
        flights = kr.json()["data"]

        if len(flights) == 0:
            return False
        else:
            cheapest = flights[0]

            route = " + ".join([leg["flyFrom"]+"-"+leg["flyTo"]+" ("+leg["airline"]+"-"+str(leg["flight_no"])+")" for leg in cheapest["route"]])
            dates = " - ".join([[leg["local_departure"] for leg in cheapest["route"]][0], [leg["local_arrival"] for leg in cheapest["route"]][-1]])
            price = cheapest["price"]
            url = cheapest["deep_link"]
            return {"price": price, "route": route, "dates": dates, "url": url}

