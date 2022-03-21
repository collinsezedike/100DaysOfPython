from flask_sqlalchemy import SQLAlchemy
from flask import Flask


class DatabaseManager:

    def __init__(self, app: Flask):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_database.db"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.db = SQLAlchemy(app)
        self.Movie = self.create_movie_table()

    def create_movie_table(self):
        class Movie(self.db.Model):
            id = self.db.Column(self.db.Integer, primary_key=True)
            title = self.db.Column(self.db.String(250), nullable=False, unique=True)
            year = self.db.Column(self.db.Integer, nullable=False)
            description = self.db.Column(self.db.String(250), nullable=False)
            img_url = self.db.Column(self.db.String(2048), nullable=False)
            rating = self.db.Column(self.db.Float)
            ranking = self.db.Column(self.db.Integer)
            review = self.db.Column(self.db.String(250))

            def __repr__(self):
                return "<Title %r>" % self.title

        # self.db.create_all()
        return Movie

    def add_new_movie(self, movie_title, year_released, movie_summary, movie_poster_url,
                      movie_rating=None, movie_ranking=None, movie_review=None):
        new_movie = self.Movie(title=movie_title, year=year_released, description=movie_summary, rating=movie_rating,
                               ranking=movie_ranking, review=movie_review, img_url=movie_poster_url)
        self.determine_movie_ranking()
        self.db.session.add(new_movie)
        self.db.session.commit()

    def get_all_movies(self):
        self.determine_movie_ranking()
        all_movies = self.db.session.query(self.Movie).order_by(self.Movie.rating).all()
        return all_movies

    def get_movie_by_id(self, movie_id):
        movie = self.Movie.query.get(movie_id)
        return movie

    def get_movie_by_title(self, movie_title):
        movie = self.Movie.query.filter_by(title=movie_title).first()
        return movie

    def edit_movie_rating_and_review(self, movie_id, new_rating, new_review):
        movie_to_edit = self.get_movie_by_id(movie_id)
        movie_to_edit.rating = new_rating
        movie_to_edit.review = new_review
        self.db.session.commit()

    def determine_movie_ranking(self):
        sorted_movie_list = self.db.session.query(self.Movie).order_by(self.Movie.rating.desc()).all()
        # sorted by rating
        for movie in sorted_movie_list:
            movie.ranking = sorted_movie_list.index(movie) + 1
            self.db.session.commit()

    def delete_movie_by_id(self, movie_id):
        movie_to_delete = self.get_movie_by_id(movie_id)
        self.db.session.delete(movie_to_delete)
        self.db.session.commit()
