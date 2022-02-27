from bs4 import BeautifulSoup
import requests

site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(site)
content = response.text

soup = BeautifulSoup(content, "html.parser")
all_movies = soup.findAll(name="h3", class_="title")
movies = [movie_tag.string for movie_tag in all_movies]
for movie in movies[::-1]:
    with open("movies.txt", "a", encoding="utf-8") as movies_file:
        movies_file.write(f"{movie}\n")
print("Done!")
