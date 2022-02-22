import requests
import datetime
from twilio.rest import Client

# CONSTANTS
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "K1GBCLB3ZOKO5LRT"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "e3cac2320ff249a1a8c9af4ee6a23b89"

ACCOUNT_SID = "ACc1e2751824a0a89117cc706d64779979"
AUTH_TOKEN = "Twilio API key"

UP_EMOJI = "🔺"
DOWN_EMOJI = "🔻"


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)

# Today is Monday and there is no data for Sunday and Saturday,
# so I'm gonna work with Friday and Thursday
test_yesterday = "2022-02-11"
test_day_before_yesterday = "2022-02-09"


news_parameters = {
    "q": COMPANY_NAME,
    "from": test_day_before_yesterday,
    "to": test_yesterday,
    "language": "en",
    "apiKey": NEWS_API_KEY,
}

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

# global variables
emoji = ""
percentage_difference = 0
headline = ""
brief = ""


def main(old_amount, new_amount):
    global emoji, percentage_difference
    # positive difference between the two prices
    difference = abs(new_amount - old_amount)
    percentage_difference = difference * 100 / old_amount
    if percentage_difference >= 5:  # 5% of day before yesterday's price
        if new_amount > old_amount:
            emoji = UP_EMOJI
        else:
            emoji = DOWN_EMOJI
        get_news()


def get_news():
    global headline, brief
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    # pick only the first three articles
    articles = response.json()["articles"]
    articles = articles[slice(3)]
    for news in articles:
        headline = news["title"]
        brief = news["description"]
        send_sms()


def send_sms():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=f"{STOCK} {emoji}{round(percentage_difference)}%\nHeadline: {headline}\nBrief: {brief}",
        from_='+18454098748',
        to='+2348129841904'
    )
    print(message.status)


def get_stock_prices():
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    response.raise_for_status()
    data = response.json()

    yesterday_closing_price = float(data["Time Series (Daily)"][test_yesterday]["4. close"])
    day_before_yesterday_closing_price = float(data["Time Series (Daily)"][test_day_before_yesterday]["4. close"])

    # angela's
    # data = response.json()["Time Series (Daily)"]
    # # convert the response data to a list so that it can data can be fetched via indices
    # data_list = [value for (key, value) in data.items()]
    # yesterday_closing_price = float(data_list[0]["4. close"])
    # day_before_yesterday_closing_price = float(data_list[1]["4. close"])

    main(old_amount=day_before_yesterday_closing_price, new_amount=yesterday_closing_price)


get_stock_prices()
