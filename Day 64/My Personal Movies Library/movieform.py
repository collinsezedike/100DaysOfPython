from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, HiddenField
from wtforms.validators import DataRequired


class RateMovieForm(FlaskForm):
    rating = FloatField("Your new rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your new review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    search = SubmitField("Add Movie")
