from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.findAll(name="a", class_="titlelink")
article_texts = []
article_links = []
for tag in article_tag:
    text = tag.getText()
    article_texts.append(text)
    link = tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]
print(article_upvotes)

most_upvoted_article = max(article_upvotes)
largest_index = article_upvotes.index(most_upvoted_article)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])
