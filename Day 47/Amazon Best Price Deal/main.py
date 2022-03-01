from bs4 import BeautifulSoup
import requests
import smtplib

site = "https://www.amazon.com/dp/B00BMR99S4/ref=sbl_dpx_office-desk-chairs_B001EJI02G_0"
my_email = "sender email"
my_password = "sender password"
recipient_email = "recipient email"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36",
}
response = requests.get(site, headers=header)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[-1])
product = soup.find(name="span", id="productTitle").getText().strip()


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Amazon Price Alert\n\n{product} is now ${price}. Buy now!\n{site}"
        )


if price >= 300:
    send_email()
