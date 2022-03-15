from flask import Flask, render_template
from myform import ContactForm

app = Flask(__name__)
app.secret_key = "Secret Key"

correct_email = "admin@email.com"
correct_password = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = ContactForm()
    if form.validate_on_submit():
        if form.email.data == correct_email and form.password.data == correct_password:
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
