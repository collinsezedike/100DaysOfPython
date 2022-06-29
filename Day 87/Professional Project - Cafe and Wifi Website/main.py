import os
from flask import Flask, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, BooleanField, SubmitField
from wtforms.validators import URL, DataRequired


def verify_api_key(entered_api_key):
    if entered_api_key == API_KEY:
        return True
    return False


API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = API_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

Bootstrap5(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(2048), nullable=False)
    img_url = db.Column(db.String(2048), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


class CafeForm(FlaskForm):
    api_key = StringField("API key", validators=[DataRequired()])
    name = StringField("Cafe name", validators=[DataRequired()])
    map_url = URLField("Cafe map URL", validators=[URL(), DataRequired()])
    img_url = URLField("Cafe image URL", validators=[URL(), DataRequired()])
    location = StringField("Cafe location (District)", validators=[DataRequired()])
    has_sockets = BooleanField("Does cafe have sockets?")
    has_toilet = BooleanField("Does cafe have toilet?")
    has_wifi = BooleanField("Does cafe have wifi?")
    can_take_calls = BooleanField("Can cafe take calls?")
    seats = StringField("How many seats does cafe have?", validators=[DataRequired()])
    coffee_price = StringField("Price for a cup of coffee", validators=[DataRequired()])
    submit = SubmitField("Add Cafe", validators=[DataRequired()])


class DeleteCafeForm(FlaskForm):
    api_key = StringField("API key", validators=[DataRequired()])
    submit = SubmitField("Delete Cafe")


@app.route("/")
def home():
    all_cafes = db.session.query(Cafe).all()
    return render_template("index.html", cafes=all_cafes)


@app.route("/new-cafe", methods=["POST", "GET"])
def new_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        if verify_api_key(form.api_key.data):
            newly_added_cafe = Cafe(name=form.name.data, map_url=form.map_url.data, img_url=form.img_url.data,
                                    location=form.location.data, has_sockets=form.has_sockets.data,
                                    has_toilet=form.has_toilet.data,
                                    has_wifi=form.has_wifi.data, can_take_calls=form.can_take_calls.data,
                                    seats=form.seats.data,
                                    coffee_price=form.coffee_price.data)
            db.session.add(newly_added_cafe)
            db.session.commit()
            flash(f"Successfully added '{newly_added_cafe.name}' to database")
            return redirect(url_for("show_cafe", cafe_id=newly_added_cafe.id))
        flash("Invalid API key")
    return render_template("new_cafe.html", form=form)


@app.route("/cafe/<int:cafe_id>")
def show_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    return render_template("cafe.html", cafe=cafe)


@app.route("/edit-cafe/<int:cafe_id>", methods=["POST", "GET"])
def edit_cafe(cafe_id):
    cafe_to_edit = Cafe.query.get(cafe_id)
    form = CafeForm(
        name=cafe_to_edit.name, map_url=cafe_to_edit.map_url, img_url=cafe_to_edit.img_url,
        location=cafe_to_edit.location,
        has_sockets=cafe_to_edit.has_sockets, has_toilet=cafe_to_edit.has_toilet, has_wifi=cafe_to_edit.has_wifi,
        can_take_calls=cafe_to_edit.can_take_calls, seats=cafe_to_edit.seats, coffee_price=cafe_to_edit.coffee_price,
    )
    form.submit.label.text = "Edit cafe data"
    if form.validate_on_submit():
        if verify_api_key(form.api_key.data):
            cafe_to_edit.name = form.name.data
            cafe_to_edit.map_url = form.map_url.data
            cafe_to_edit.img_url = form.img_url.data
            cafe_to_edit.location = form.location.data
            cafe_to_edit.has_sockets = form.has_sockets.data
            cafe_to_edit.has_toilet = form.has_toilet.data
            cafe_to_edit.has_wifi = form.has_wifi.data
            cafe_to_edit.can_take_calls = form.can_take_calls.data
            cafe_to_edit.seats = form.seats.data
            cafe_to_edit.coffee_price = form.coffee_price.data
            db.session.commit()
            flash(f"Changes saved successfully")
            return redirect(url_for("show_cafe", cafe_id=cafe_to_edit.id))
        flash("Invalid API key")
    return render_template("cafe.html", cafe=cafe_to_edit, form=form, to_edit=True)


@app.route("/delete-cafe/<int:cafe_id>", methods=["POST", "GET"])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    cafe_name = cafe_to_delete.name
    form = DeleteCafeForm()
    if form.validate_on_submit():
        if verify_api_key(form.api_key.data):
            db.session.delete(cafe_to_delete)
            db.session.commit()
            flash(f"Successfully deleted '{cafe_name}' from database")
            return redirect(url_for("home"))
        flash("Invalid API key")
    return render_template("cafe.html", cafe=cafe_to_delete, form=form, to_delete=True)


if __name__ == "__main__":
    app.run()
