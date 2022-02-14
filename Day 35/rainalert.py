import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "4d98863abc9a025d03bd24075f4fe41c"
MY_LAT = 6.524379
MY_LONG = 3.379206
ACCOUNT_SID = "ACc1e2751824a0a89117cc706d64779979"
AUTH_TOKEN = "ce91010da40ddbc4241ea511087ded0e"

test_lat = -15.826691
test_long = -47.921822

parameters = {
    "lat": test_lat,
    "lon": test_long,
    "exclude": ["current", "minutely", "daily"],
    "appid": API_KEY,
}

response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json().get("hourly")

# id_list = []
# for item in weather_data[:12]:
#     weather_id = item["weather"][0]["id"]
#     id_list.append(weather_id)

# using list comprehension
id_list = [item["weather"][0]["id"] for item in weather_data[:12]]

will_rain = False
for id in id_list:
    if id <= 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="\n\nIt's going to 🌧️ today. Remember to bring an ☂️.",
        from_='+18454098748',
        to='+2348129841904'
    )

    print(message.status)
