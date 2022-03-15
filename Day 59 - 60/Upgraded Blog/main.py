from flask import Flask, render_template, request
import requests
import smtplib

BLOG_ENDPOINT = "https://api.npoint.io/8223e6b05e7d05dd2670"

response = requests.get(BLOG_ENDPOINT)
blog_data = response.json()

my_email = "sender email"
my_password = "sender password"
recipient_email = "recipient email"


def send_message(user_name, user_email, user_phone_number, user_message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:New message\n\n"
                f"Name:{user_name}\nEmail:{user_email}\nPhone:{user_phone_number}\nMessage{user_message}"
        )


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", blog_posts=blog_data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        name, email, phone_number, message = data["name"], data["email"], data["phone"], data["message"]
        send_message(name, email, phone_number, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:post_id>")
def post_page(post_id):
    for post in blog_data:
        if post["id"] == post_id:
            return render_template("post.html", post_content=post)


if __name__ == "__main__":
    app.run(debug=True)
