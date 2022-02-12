import datetime as dt
import random
import smtplib
from workingwithemailsmtp import my_email, my_password, recipient_email


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:Stay Motivated\n\n{quote_for_the_day}")


with open("Birthday Wisher/quotes.txt") as quotes_file:
    quotes = [quote.strip() for quote in quotes_file.readlines()]

quote_for_the_day = random.choice(quotes)
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 4:
    send_mail()


