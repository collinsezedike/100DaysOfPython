import requests

API_KEY = "MY API KEY"
MY_LAT = 6.524379
MY_LONG = 3.379206

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
}

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

