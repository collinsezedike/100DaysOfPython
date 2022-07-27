from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


def get_definition(word: str):
    API_ENDPOINT = f"https://owlbot.info/api/v4/dictionary/{word}"
    API_TOKEN = os.getenv("API_TOKEN")

    header = {
        "accept-encoding": "utf-8",
        "Authorization": f"Token {API_TOKEN}",
    }
    
    return requests.get(API_ENDPOINT, headers=header)


class SearchForm(FlaskForm):
    word = SearchField("", validators=[DataRequired()])
    search = SubmitField("Search", validators=[DataRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)


@app.route("/", methods=["GET","POST"])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        word = form.word.data
        return redirect(url_for("define", word=word))
    return render_template("index.html", form=form)
    

@app.route("/definition/<word>")
def define(word):
    
    is_invalid = False

    response = get_definition(word)
    if response.status_code == 200:
        response = response.json()
    elif response.status_code == 404:
        is_invalid = (True, word)

    return render_template("response.html", 
                            is_invalid=is_invalid, 
                            response=response)


if __name__ == "__main__":
    app.run()
