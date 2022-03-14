from flask import Flask, render_template
import requests
import random
from datetime import datetime


developer = "Collins Ezedike-egwom"
app = Flask(__name__)


def get_age(name):
    response = requests.get("https://api.agify.io/", params={"name": name})
    data = response.json()
    return data["age"]


def get_gender(name):
    response = requests.get("https://api.genderize.io/", params={"name": name})
    data = response.json()
    return data["gender"]


def get_blog_posts():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return data


@app.route("/")
def home_page():
    random_number = random.randint(0, 9)
    year = datetime.now().year
    return render_template("index.html", num=random_number, current_year=year, name=developer)


@app.route("/guess/<name>")
def guess_page(name):
    user_name = name
    guessed_age = get_age(name)
    guessed_gender = get_gender(name)
    return render_template("guess.html", name=user_name, age=guessed_age, gender=guessed_gender)


@app.route("/blog")
def blog_page():
    posts = get_blog_posts()
    return render_template("blog.html", blog_posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
