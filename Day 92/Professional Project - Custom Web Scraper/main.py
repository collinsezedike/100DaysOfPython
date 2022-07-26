import csv
import requests

from bs4 import BeautifulSoup

site = "https://www.audible.com/search?keywords=book&node=18573211011"

response = requests.get(site)
response.raise_for_status()
site_content = response.text

soup = BeautifulSoup(site_content, "html.parser")

title_tags = soup.select(".bc-heading .bc-color-link")   
author_tags = soup.select(".authorLabel .bc-size-small")
narrator_tags = soup.select(".narratorLabel .bc-size-small")
length_tags = soup.select(".runtimeLabel .bc-size-small")
release_date_tags = soup.select(".releaseDateLabel .bc-size-small")
language_tags = soup.select(".languageLabel .bc-size-small")
price_tags = soup.select(".buybox-regular-price .bc-size-base")
review_tags = soup.select(".ratingsLabel .bc-pub-offscreen")
rating_count_tags = soup.select(".ratingsLabel .bc-size-small")

# To remove irrelevant tags: 'Regular Price' and 'or 1 credit'
for tag in price_tags:
    if "$" not in tag.get_text():
        price_tags.remove(tag)

books = []

for index, (title_tag, author_tag, narrator_tag, 
            length_tag, release_date_tag, language_tag, 
            price_tag, review_tag, rating_count_tag) in enumerate(zip(title_tags, author_tags, narrator_tags,
                                                                      length_tags, release_date_tags, language_tags, 
                                                                      price_tags, review_tags, rating_count_tags)):
    book_info = {   
                "s/n": index+1,
                "title": title_tag.get_text().strip(),
                "author": author_tag.get_text().replace("By:", " ").strip(),
                "narrator": narrator_tag.get_text().replace("Narrated by:", " ").strip(),
                "length": length_tag.get_text().replace("Length:", " ").strip(),
                "release date": release_date_tag.get_text().replace("Release date:", " ").strip(),
                "language": language_tag.get_text().replace("Language:", " ").strip(),
                "price": price_tag.get_text().strip(),
                "review": review_tag.get_text().strip(),
                "ratings": rating_count_tag.get_text().strip()
            }
    books.append(book_info)
    
    
with open('data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=book_info.keys())
    writer.writeheader()
    writer.writerows(books)
