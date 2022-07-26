from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_bootstrap import Bootstrap5
import os
from werkzeug.utils import secure_filename

from sklearn.cluster import KMeans
import cv2
from collections import Counter


def extract_colors(img_file, num_colors=10):
    def RGB2HEX(color):
        return f"#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}"

    image = cv2.imread(img_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_width = image.shape[0]
    img_height = image.shape[1]

    reshaped_image = cv2.resize(image, (img_width // 10, img_height // 10))
    reshaped_image = reshaped_image.reshape(
        reshaped_image.shape[0] * reshaped_image.shape[1], 3
    )

    clf = KMeans(n_clusters=num_colors)
    labels = clf.fit_predict(reshaped_image)
    counts = Counter(labels)
    counts = dict(sorted(counts.items()))
    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    return hex_colors


app = Flask(__name__)
app.config["SECRET_KEY"] = "asecretkey"

app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 10
app.config["UPLOAD_EXTENSIONS"] = [".jpg"]
app.config["UPLOAD_PATH"] = "static/upload"
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/upload-image", methods=["GET", "POST"])
def recieve_image():
    session.clear()
    if request.method == "POST":
        image = request.files["image"]
        if image:
            filename = secure_filename(image.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    flash("Image must be a .jpg type")
                else:
                    filename = f"image{file_ext}"
                    image.save(os.path.join(app.config["UPLOAD_PATH"], filename))
                    img_file = f"{app.config['UPLOAD_PATH']}/image.jpg"
                    session["colors"] = extract_colors(img_file)
                    return redirect(url_for("display_palette"))
            else:
                flash("Invalid file")
        else:
            flash("This field is required!")
    return render_template("upload_image.html")


@app.route("/color-palette/")
def display_palette():
    return render_template("colors.html")


if __name__ == "__main__":
    app.run(debug=True)
