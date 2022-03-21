from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

# local imports
from database_manager import DatabaseManager
from movieform import RateMovieForm, AddMovieForm
from movie_finder import MovieFinder

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap(app)
database_manager = DatabaseManager(app)
movie_finder = MovieFinder()


@app.route("/")
def home():
    if request.args.get("id"):
        movie_id = request.args.get("id")
        database_manager.delete_movie_by_id(movie_id)
    all_movies = database_manager.get_all_movies()
    return render_template("index.html", movies_list=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_rating_and_review():
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = request.form["id"]
        new_rating = form.rating.data
        new_review = form.review.data
        database_manager.edit_movie_rating_and_review(movie_id, new_rating, new_review)
        return redirect(url_for('home'))
    movie_id = request.args.get("id")
    movie_to_be_edited = database_manager.get_movie_by_id(movie_id)
    return render_template("edit.html", movie=movie_to_be_edited, form=form)


@app.route("/add", methods=["POST", "GET"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_to_search_for = form.movie_title.data
        search_result = movie_finder.search_for_movie(movie_to_search_for)
        return render_template("select.html", search_result=search_result)
    elif request.args.get("id"):
        movie_id = request.args.get("id")
        selected_movie_data = movie_finder.get_movie_data(movie_id)
        database_manager.add_new_movie(
            selected_movie_data["title"],
            selected_movie_data["release_date"].split("-")[0],
            selected_movie_data["overview"],
            f'https://image.tmdb.org/t/p/w500/{selected_movie_data["poster_path"]}',
        )
        movie = database_manager.get_movie_by_title(selected_movie_data["title"])
        form = RateMovieForm()
        return render_template("edit.html", form=form, movie=movie)
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
