from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test-SQLAlchemy-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<Books %r>' % self.title


# db.create_all()
row = Books(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(row)
db.session.commit()
