import datetime as dt

now = dt.datetime.now()
# to get today's year
year = now.year
if year == 2022:
    print("Learn Python")

# to get today's month
month = now.month
day_of_week = now.weekday()


# create your own datetime
date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)

