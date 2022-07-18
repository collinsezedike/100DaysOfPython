import os
from datetime import datetime

from flask import Flask, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from forms import SignUpForm, SignInForm, DateForm, TaskForm, UsernameForm


def convert_str_date_to_dt_date(str_date: str):
    """The String date should be passed in the format: 'YYYY-MM-DD'\n
    Returns a datetime object of the string date"""
    str_date_split_list = str_date.split("-")
    year = int(str_date_split_list[0])
    month = int(str_date_split_list[1])
    day = int(str_date_split_list[2])
    dt_date = datetime(year, month, day)
    return dt_date


def check_if_date_is_past(date: datetime):
    present_date = datetime.now().strftime("%Y-%m-%d")
    return convert_str_date_to_dt_date(present_date) > date


def sort_tasks(task_list):
    return [task for task in task_list if task.category == "Foremost"], \
           [task for task in task_list if task.category == "Crucial"], \
           [task for task in task_list if task.category == "Important"], \
           [task for task in task_list if task.category == "Minor"]


app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)

uri = os.getenv("DATABASE_URL", "sqlite:///database.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tasks = db.relationship("Task")


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    is_done = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return render_template("index.html")


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

        hashed_password = generate_password_hash(password=form.password.data,
                                                 method="pbkdf2:sha256",
                                                 salt_length=8)
        new_user = User(name=form.name.data.title(),
                        username=form.username.data.lower(),
                        email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("dashboard"))
    return render_template("register.html", form=form)


@app.route("/sign-in", methods=["GET", "POST"])
def login():
    form = SignInForm()
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
            return redirect(url_for("dashboard"))

    return render_template("login.html", form=form)


@app.route("/sign-out")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/dashboard")
@app.route("/dashboard/")
@login_required
def dashboard():
    """Redirects to dashboard_date"""
    return redirect(url_for("dashboard_date", date=datetime.now().strftime("%Y-%m-%d")))


@app.route("/dashboard/<date>")
@login_required
def dashboard_date(date):
    date = convert_str_date_to_dt_date(date)
    tasks = Task.query.filter_by(date=date).all()
    return render_template("dashboard.html", tasks=tasks,
                           foremost_task=sort_tasks(tasks)[0],
                           crucial_tasks=sort_tasks(tasks)[1],
                           important_tasks=sort_tasks(tasks)[2],
                           minor_tasks=sort_tasks(tasks)[3],
                           date_is_past=check_if_date_is_past(date))


@app.route("/dashboard/select-date", methods=["GET", "POST"])
def select_date():
    form = DateForm(date=datetime.now())
    if form.validate_on_submit():
        print(form.date.data)
        print(type(form.date.data))
        return redirect(url_for("dashboard_date", date=form.date.data))
    return render_template("blank_form.html", form=form)


@app.route("/dashboard/add-task", methods=["GET", "POST"])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(task=form.task.data,
                        category=form.category.data,
                        date=form.date.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("dashboard_date", date=form.date.data))
    form.date.data = datetime.now()
    return render_template("blank_form.html", form=form)


@app.route("/dashboard/edit-username", methods=["GET", "POST"])
def edit_username():
    form = UsernameForm(username=current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("blank_form.html", form=form)


@app.route("/dashboard/edit-task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get(task_id)
    form = TaskForm(task=task.task, category=task.category, date=task.date)
    form.submit.label.text = "Edit task"
    if form.validate_on_submit():
        task.task = form.task.data
        task.category = form.category.data
        task.date = form.date.data
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("blank_form.html", form=form)


@app.route("/dashboard/done/<task_id>")
def cross_task(task_id):
    task = Task.query.get(task_id)
    task.is_done = not task.is_done
    db.session.commit()
    return redirect(url_for("dashboard"))


@app.route("/dashboard/delete-task/<task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run()
