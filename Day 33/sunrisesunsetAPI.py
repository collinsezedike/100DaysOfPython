import requests

MY_LAT = 6.524379
MY_LONG = 3.379206

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_time = sunrise.split("T")
sunrise_hour = sunrise_time[1].split(":")[0]

sunset_time = sunset.split("T")
sunset_hour = sunset_time[1].split(":")[0]

print(sunrise_hour)
print(sunset_hour)
