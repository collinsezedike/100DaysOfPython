from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as website:
    contents = website.read()

# create a beautiful soup object
soup = BeautifulSoup(contents, "html.parser")
# get hold of a tag
print(soup.title)   # in this case, the title tag
# to get a tag name
print(soup.title.name)
# to get the text inside a tag
print(soup.title.string)
# to format the code nicely with indentation
print(soup.prettify())

# to get all occurrences if a tag
all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    # to get the value of an attribute of a tag
    print(tag.get("href"))

header = soup.find(name="h1", id="name")
print(header)

# Note: Because "class" is a python keyword already,
# it cannot be used as a keyword argument.
# "class_" is used instead, without the quotation marks
h3_heading = soup.find(name="h3", class_="heading")
print(h3_heading)
# I believe this is also the reason why
# twilio sender number keyword is
# "from_" not "from"

# using css selector to get hold of a tag
company_url = soup.select_one(selector="p a")
print(company_url)
# selecting by id
name = soup.select_one(selector="#name")
print(name)
# selecting by class
headings = soup.select(selector=".heading")
print(headings)
