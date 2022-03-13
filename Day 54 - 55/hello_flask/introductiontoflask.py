from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper(**kwargs):
        return f"<b>{func(**kwargs)}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper(**kwargs):
        return f"<em>{func(**kwargs)}</em>"
    return wrapper


def make_underlined(func):
    def wrapper(**kwargs):
        return f"<u>{func(**kwargs)}</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "<p>Bye</p>"


@app.route("/<name>/<int:age>")
@make_bold
@make_emphasis
@make_underlined
def greet(name, age):
    return f"<p>Hello {name.title()}, You are {age} years old.</p>"


if __name__ == "__main__":
    app.run(debug=True)
