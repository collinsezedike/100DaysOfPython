from twilio.rest import Client
from flight_data import FlightData
import smtplib

ACCOUNT_SID = "ACc1e2751824a0a89117cc706d64779979"
AUTH_TOKEN = "fb6e8a801f43d9d41e12362a72558c43"
MY_EMAIL = "senderemail@gmail.com"
MY_PASSWORD = "sender password"

currency = "£"


class NotificationManager:

    def __init__(self, flight_data: FlightData):
        self.message = f"Low price alert! Only {currency.encode('utf-8')}{flight_data.price} to fly " \
                       f"from {flight_data.origin_city}-{flight_data.origin_airport} " \
                       f"to {flight_data.destination_city}-{flight_data.destination_airport}, " \
                       f"from {flight_data.departure_date} to {flight_data.return_date}"
        self.email = f"Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} " \
                     f"to {flight_data.destination_city}-{flight_data.destination_airport}, " \
                     f"from {flight_data.departure_date} to {flight_data.return_date}"
        self.link = \
            f"https://www.google.co.uk/flights?hl=en#flt=" \
            f"{flight_data.origin_airport}.{flight_data.destination_airport}.{flight_data.departure_date}" \
            f"*{flight_data.destination_airport}.{flight_data.origin_airport}.{flight_data.return_date}"

    def send_sms(self):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            body=self.message,
            from_="+18454098748",
            to="+2348129841904"
        )

    def send_email(self, email):
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Low Price Alert!\n\n{self.email}\n{self.link}"
                )
        except:
            print("Something went wrong! Email not sent.")
