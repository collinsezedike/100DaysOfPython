from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookshelf.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<Books %r>" % self.title


# db.create_all()
# row = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(row)
# db.session.commit()


@app.route('/')
def home():
    if request.args.get("id"):
        book_id = request.args.get("id")
        book_to_delete = Books.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()

    all_books = db.session.query(Books).all()
    return render_template("index.html", books_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book_data = dict()
        new_book_data["title"] = request.form["bookName"].title()
        new_book_data["author"] = request.form["bookAuthor"].title()
        new_book_data["rating"] = request.form["bookRating"]

        new_record = Books(title=new_book_data["title"], author=new_book_data["author"], rating=new_book_data["rating"])
        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        book_id = request.form["id"]
        new_rating = request.form["newRating"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_to_be_updated = Books.query.get(book_id)
    return render_template("edit.html", book=book_to_be_updated)


if __name__ == "__main__":
    app.run(debug=True)
