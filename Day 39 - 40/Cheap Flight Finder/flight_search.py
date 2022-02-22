import requests
from flight_data import FlightData

TEQUILA_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "JLrHrWyrIqJWUdetWJ_yjMzfUKTcnr3o"


class FlightSearch:

    def __init__(self):
        self.header = {"apikey": TEQUILA_API_KEY}

    def get_destination_code(self, city):
        query = {"term": city, "location_types": "city"}
        response = requests.get(TEQUILA_LOCATION_ENDPOINT, params=query, headers=self.header)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def search_for_flight(self, origin_city_code, destination_city_code, from_time, to_time):

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "data_from": from_time,
            "data_to": to_time,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=query, headers=self.header)
        try:
            response_data = response.json()["data"][0]
        except IndexError:
            try:
                query["max_stopovers"] = 1
                response_data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}")
                return None
            else:
                going_route_data = response_data["route"][0]
                stop_over_data = response_data["route"][1]
                returning_route_data = response_data["route"][2]
                flight_data = FlightData(
                    price=response_data["price"],
                    origin_city=going_route_data["cityFrom"],
                    origin_airport=going_route_data["flyFrom"],
                    destination_city=stop_over_data["cityTo"],
                    destination_airport=stop_over_data["flyTo"],
                    departure_date=going_route_data["local_departure"].split("T")[0],
                    return_date=returning_route_data["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=going_route_data["cityTo"]
                )
                return flight_data
        else:
            going_route_data = response_data["route"][0]
            returning_route_data = response_data["route"][1]
            flight_data = FlightData(
                price=response_data["price"],
                origin_city=going_route_data["cityFrom"],
                origin_airport=going_route_data["flyFrom"],
                destination_city = going_route_data["cityTo"],
                destination_airport=going_route_data["flyTo"],
                departure_date=going_route_data["local_departure"].split("T")[0],
                return_date=returning_route_data["local_departure"].split("T")[0]
            )
            return flight_data
