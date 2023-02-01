import requests
import datetime

# This connects to the api
response = requests.get(url = "http://api.open-notify.org/iss-now.json")

# if the response code is anything but 200 (success), raise an exception:
# (compare for example what happens if the url has a mistake: it raises a 404)
response.raise_for_status()

data = response.json()

lat = float(data["iss_position"]["latitude"])
lon = float(data["iss_position"]["longitude"])

location = (lat, lon)
print(location)

# ------------- sunset and sunrise ----------------

parameters = {"lat": 3.2579283267853185,
              "lng": -76.57078066276841,
              "formatted": 0} # 24-h clock

response2 = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
response2.raise_for_status()

sunset_data = response2.json()
print(sunset_data)
sunset = sunset_data["results"]["sunset"]
sunrise = sunset_data["results"]["sunrise"]

sunset = sunset.split("+")
sunset = datetime.datetime.strptime(sunset[0], "%Y-%m-%dT%H:%M:%S") - datetime.timedelta(hours = 5)

sunrise = sunrise.split("+")
sunrise = datetime.datetime.strptime(sunrise[0], "%Y-%m-%dT%H:%M:%S") - datetime.timedelta(hours = 5)
