import requests
from bs4 import BeautifulSoup

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36",
}


class HouseFinder:

    def __init__(self, site):
        response = requests.get(site, headers=header)
        content = response.text
        self.soup = BeautifulSoup(content, "html.parser")
        self.house_data = {}

    def get_house_data(self):
        house_addresses = self.get_house_addresses()
        house_links = self.get_house_links()
        house_prices = self.get_house_prices()
        for index in range(len(house_prices)):
            self.house_data[index] = {
                "price": house_prices[index],
                "address": house_addresses[index],
                "link": house_links[index],
            }

    def get_house_links(self):
        anchor_tags = self.soup.findAll(name="a", class_="list-card-link")
        links = [tags.get("href") for tags in anchor_tags]

        for link in links:
            if not link.startswith("https://www.zillow.com"):
                links_with_https = "https://www.zillow.com" + link
                links.insert(links.index(link), links_with_https)
                links.remove(link)
        links_without_duplicates = list(dict.fromkeys(links))
        return links_without_duplicates

    def get_house_prices(self):
        div_tags = self.soup.findAll(name="div", class_="list-card-price")
        prices = [tags.getText().replace("+", "").replace("/mo", "").replace("1 bd", "").strip() for tags in div_tags]
        return prices

    def get_house_addresses(self):
        address_tags = self.soup.findAll(name="address", class_="list-card-addr")
        addresses = [tags.getText() for tags in address_tags]
        return addresses
