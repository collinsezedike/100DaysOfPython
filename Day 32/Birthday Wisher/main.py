import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "sender@gmail.com"
MY_PASSWORD = "sender password"

# TODO 1: Read and descramble the csv
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

# TODO 2: Compare all the date of births from the csv with the current date
now = dt.datetime.now()
for profile in birthdays:
    if profile["month"] == now.month and profile["day"] == now.day:
        celebrant_name = profile["name"]
        celebrant_email = profile["email"]

        # TODO 3: Choose a random message to send
        message_files = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
        with open(random.choice(message_files)) as msg_file:
            with open("mail_file.txt", "w") as mail_file:
                for line in msg_file.readlines():
                    mail_file.write(line.replace("[NAME]", celebrant_name.title()))

        with open("mail_file.txt") as mail:
            message = mail.read()
        try:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=celebrant_email, msg=message)
        except:
            print("Something went wrong!")
        else:
            connection.close()



