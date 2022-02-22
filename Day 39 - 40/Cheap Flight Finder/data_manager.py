import requests

SHEETY_FLIGHTS_ENDPOINT = "https://api.sheety.co/4f19d4f3096bb433d01a8f806c80f6db/flightDeals(100DaysOfCode)/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/4f19d4f3096bb433d01a8f806c80f6db/flightDeals(100DaysOfCode)/users"


class DataManager:

    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(SHEETY_FLIGHTS_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=f"{SHEETY_FLIGHTS_ENDPOINT}/{city['id']}", json=new_data)

    def add_new_user(self, f_name, l_name, email):
        new_user = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email,
            }
        }
        requests.post(SHEETY_USERS_ENDPOINT, json=new_user)

    def get_users_emails(self):
        response = requests.get(SHEETY_USERS_ENDPOINT)
        data = response.json()["users"]
        email_list = [user["email"] for user in data]
        return email_list
