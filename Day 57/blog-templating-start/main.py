from flask import Flask, render_template
from post import Post

app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    all_blog_posts = posts.get_all_posts()
    return render_template("index.html", blog_posts=all_blog_posts)


@app.route("/post/<int:post_id>")
def open_blog_post(post_id):
    post_content = posts.get_post_by_id(post_id)
    return render_template("post.html", post=post_content)


if __name__ == "__main__":
    app.run(debug=True)
