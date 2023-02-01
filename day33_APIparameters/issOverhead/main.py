import requests
import datetime
from time import sleep
import smtplib
from password import gmail_password

MY_LAT = 3.2579283267853185 # Your latitude
MY_LONG = -76.57078066276841 # Your longitude
MY_EMAIL = "testpythongp@gmail.com"

# ------------- functions --------------

def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return {"lat": iss_latitude, "lng": iss_longitude}

def is_iss_close(iss_location):
    dif_lat = abs(iss_location["lat"] - MY_LAT)
    dif_lng = abs(iss_location["lng"] - MY_LONG)
    if dif_lat <= 5 and dif_lng <= 5:
        return True
    else:
        return False

def get_sunset_data():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunset_data = response.json()

    sunset = sunset_data["results"]["sunset"].split("+")
    sunrise = sunset_data["results"]["sunrise"].split("+")

    sunset = datetime.datetime.strptime(sunset[0], "%Y-%m-%dT%H:%M:%S") - datetime.timedelta(hours = 5)
    sunrise = datetime.datetime.strptime(sunrise[0], "%Y-%m-%dT%H:%M:%S") - datetime.timedelta(hours = 5)
    return {"sunset": sunset, "sunrise": sunrise}

    
def is_dark(sunset_data):
    actual_time = datetime.datetime.now()
    if actual_time <= sunset_data["sunrise"] or actual_time >= sunset_data["sunset"]:
        return True
    else:
        return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = gmail_password)
        connection.sendmail(MY_EMAIL, "testpythongp@outlook.com", "Subject:Look up the ISS!\n\nThe ISS is fairly over your head. Look up.")


# ------------------ Main loop ----------------------

while True:
    il = get_iss_location()
    sd = get_sunset_data()
    if is_iss_close(il) and is_dark(sd):
        send_email()
    at = datetime.datetime.now()
    print(at)
    sleep(60) #seconds


