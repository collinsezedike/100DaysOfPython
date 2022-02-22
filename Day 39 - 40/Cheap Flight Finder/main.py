from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta

DATE_FORMAT = "%d/%m/%Y"
ORIGIN_CITY = "LON"
next_day = (datetime.now() + timedelta(days=+1)).strftime(DATE_FORMAT)
six_months_later = (datetime.now() + timedelta(days=(30 * 6))).strftime(DATE_FORMAT)

flight_search = FlightSearch()
data_manager = DataManager()


def new_sign_up():
    print("Welcome to The Beyond Flight Code")
    print("We find the best flight and email you!")
    first_name = input("What is your first name? ").title()
    last_name = input("What is your last name? ").title()
    valid_email = False
    while not valid_email:
        email = input("What is your email address? ").lower()
        confirm_email = input("Confirm your email address? ").lower()
        if email == confirm_email:
            valid_email = True
        else:
            print("Different email entries")
    print(f"\nYou've been added to the club, {first_name}!")
    print("Expect the best flight deals you can ever get in the world.")
    print("Be sure not to miss our emails.")
    data_manager.add_new_user(first_name, last_name, email)


sheet_flight_data = data_manager.get_destination_data()
for row in sheet_flight_data:
    row["iataCode"] = flight_search.get_destination_code(row["city"])
data_manager.destination_data = sheet_flight_data
data_manager.update_destination_code()

new_sign_up()

for city in sheet_flight_data:
    flight = flight_search.search_for_flight(
        origin_city_code=ORIGIN_CITY,
        destination_city_code=city["iataCode"],
        from_time=next_day,
        to_time=six_months_later
    )
    if flight is None:
        pass

    if flight.price <= city["lowestPrice"]:
        notification_manager = NotificationManager(flight_data=flight)
        users_emails = data_manager.get_users_emails()
        for recipient_email in users_emails:
            if flight.stop_overs > 0:
                notification_manager.email += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            notification_manager.send_email(recipient_email)
