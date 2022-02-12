import requests

# make an API request to the International Space Station to get data about it
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# to raise an exception if there was an error
response.raise_for_status()

# to retrieve the data
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
