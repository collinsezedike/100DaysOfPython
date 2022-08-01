from flask import Flask, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from werkzeug.security import generate_password_hash, check_password_hash

import requests
import os


def add_products_to_database():
    response = requests.get("https://fakestoreapi.com/products")
    data = response.json()
    for product in data:
        new_product = Product(name=product["title"], price=product["price"], description=product["description"], img_url=product["image"])
        db.session.add(new_product)
        db.session.commit()


class SignUpForm(FlaskForm):
    name = StringField("", render_kw={"placeholder": "Name"}, validators=[DataRequired()])
    email = EmailField("", render_kw={"placeholder": "Email address"}, validators=[DataRequired(), Email()])
    password = PasswordField("", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    confirm_password = PasswordField("", render_kw={"placeholder": "Confirm Password"}, validators=[DataRequired()])
    submit = SubmitField("Sign up", render_kw={"class": "primary-button"}, validators=[DataRequired()])


class SignInForm(FlaskForm):
    email = EmailField("", render_kw={"placeholder": "Email address"}, validators=[DataRequired(), Email()])
    password = PasswordField("", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField("Sign in", render_kw={"class": "primary-button"}, validators=[DataRequired()])


uri = os.getenv("DATABASE_URL", "sqlite:///database.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap5(app)

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    cart = db.relationship("Cart")


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String(2048), nullable=False)


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(2048), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


db.create_all()
if not db.session.query(Product).all(): # if data is empty
    add_products_to_database()
    

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    products = db.session.query(Product).all()
    return render_template("index.html", products=products)


@app.route("/product/<product_id>")
def show_product(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product)

    
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sign-up", methods=["GET", "POST"])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():  # check if user already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
        elif form.password.data != form.confirm_password.data:
            flash("Password and confirm password are not the same")
            return redirect(url_for("register"))
        else:
            protected_password = generate_password_hash(password=form.password.data,
                                                        method="pbkdf2:sha256",
                                                        salt_length=8)
            new_user = User(name=form.name.data.title(),
                            email=form.email.data,
                            password=protected_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("show_cart"))
    return render_template("login.html", form=form, register_form=True)


@app.route("/sign-in", methods=["GET", "POST"])
def login():
    form=SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if not user:  # if user does not exist
            flash("No account found with such email. Create an account now.")
            return redirect(url_for("register"))
        elif not check_password_hash(user.password, password):
            flash("Password is incorrect. Please try again.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("show_cart"))

    return render_template("login.html", form=form)


@app.route("/sign-out")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/cart")
def show_cart():
    if not current_user.is_authenticated:
        flash("You need to be logged in!")
        return redirect(url_for("login"))
    else:
        cart = Cart.query.all()
        print(len(cart))
        return render_template("cart.html", cart=cart)


@app.route("/cart/add/<product_id>")
def add_to_cart(product_id):
    if not current_user.is_authenticated:
        return redirect(url_for("show_cart"))
    else:
        item_to_add = Product.query.get(product_id)
        if Cart.query.filter_by(name=item_to_add.name).first():  # check if item is already in cart
            cart_item =  Cart.query.filter_by(name=item_to_add.name).first()
            cart_item.quantity += 1
            db.session.commit()
        else:
            new_cart_item = Cart(name=item_to_add.name, 
                                    price=item_to_add.price,
                                    description=item_to_add.description, 
                                    img_url=item_to_add.img_url,
                                    quantity=1)
            db.session.add(new_cart_item)
            db.session.commit()
        return redirect(url_for("home"))


@app.route("/cart/increment/<cart_item_id>")
@login_required
def increase_cart_item_quantity(cart_item_id):
    item_to_increment = Cart.query.get(cart_item_id)
    item_to_increment.quantity += 1
    db.session.commit()
    return redirect(url_for("show_cart"))


@app.route("/cart/decrement/<cart_item_id>")
@login_required
def decrease_cart_item_quantity(cart_item_id):
    item_to_decrement = Cart.query.get(cart_item_id)
    if item_to_decrement.quantity > 1:
        item_to_decrement.quantity -= 1
    else:
        db.session.delete(item_to_decrement)
    db.session.commit()
    return redirect(url_for("show_cart"))


@app.route("/cart/remove/<cart_item_id>")
@login_required
def remove_from_cart(cart_item_id):
    item_to_remove = Cart.query.get(cart_item_id)
    db.session.delete(item_to_remove)
    db.session.commit()
    return redirect(url_for("show_cart"))


@app.route("/checkout")
@login_required
def checkout():
    return render_template("checkout.html")


if __name__ == "__main__":
    app.run()
