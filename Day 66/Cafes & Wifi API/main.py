from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def make_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    number_of_cafes = len(db.session.query(Cafe).all())
    random_cafe_id = random.randint(1, number_of_cafes)
    random_cafe = Cafe.query.get(random_cafe_id)

    return jsonify(cafe=random_cafe.make_dict())


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    all_cafes_dict = [cafe.make_dict() for cafe in all_cafes]
    return jsonify(cafes=all_cafes_dict)


@app.route("/search")
def search_for_cafe():
    if request.args.get("loc"):
        search_location = request.args.get("loc")
        cafe_in_search_location = Cafe.query.filter_by(location=search_location).first()
        if cafe_in_search_location:
            return jsonify(cafe=cafe_in_search_location.make_dict())
        return jsonify(error={"Not Found": "Sorry, we don't a cafe at that location."}), 404
    return jsonify(error={"Invalid request": "Missing parameters"}), 400


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    cafe = request.form["name"]
    map_url = request.form["map_url"]
    img_url = request.form["img_url"]
    location = request.form["location"]
    seats = request.form["seats"]
    has_toilet = request.form["has_toilet"]
    has_wifi = request.form["has_wifi"]
    has_sockets = request.form["has_sockets"]
    can_take_calls = request.form["can_take_calls"]
    coffee_price = request.form["coffee_price"]
    print(request.form)
    new_cafe = Cafe(name=cafe, map_url=map_url, img_url=img_url, location=location, seats=seats,
                    has_toilet=bool(has_toilet), has_wifi=bool(has_wifi), has_sockets=bool(has_sockets),
                    can_take_calls=bool(can_take_calls), coffee_price=coffee_price)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    if Cafe.query.get(cafe_id):
        cafe = Cafe.query.get(cafe_id)
        if request.args.get("new_price"):
            new_price = request.args.get("new_price")
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(success="Successfully updated the price"), 200
        return jsonify(error={"Invalid request": "Missing or invalid parameters"}), 400
    return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database"}), 404


# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if Cafe.query.get(cafe_id):
        cafe = Cafe.query.get(cafe_id)
        if request.args.get("api_key") == "TopSecretAPIKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Cafe successfully deleted from database"), 200
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api key."), 403
    return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database"}), 404


if __name__ == '__main__':
    app.run(debug=True)
