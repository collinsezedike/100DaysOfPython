import requests
from datetime import datetime
from math import floor
import smtplib
import time

MY_LAT = 6.524379
MY_LONG = 3.379206
MY_EMAIL = "senderemail@gmail.com"
MY_PASSWORD = "sender password"
RECIPIENT = "recipientemail@email.com"


def iss_overhead():
    """Checks if ISS is overhead. Returns True or False"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    longitude_range = range(floor(MY_LONG)-5, floor(MY_LONG)+5)
    latitude_range = range(floor(MY_LAT)-5, floor(MY_LONG)+5)
    if floor(iss_longitude) in longitude_range and floor(iss_latitude) in latitude_range:
        return True
    else:
        return False


def is_dark():
    """Checks if it is currently dark. Returns True or False"""

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    else:
        return False


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_PASSWORD,
            msg="Subject:ISS Overhead!\n\nLook up!"
        )


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        send_mail()
