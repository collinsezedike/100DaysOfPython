from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email


class SignUpForm(FlaskForm):
    name = StringField("", render_kw={"placeholder": "Full name"}, validators=[DataRequired()])
    username = StringField("", render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    email = EmailField("", render_kw={"placeholder": "Email address"}, validators=[DataRequired(), Email()])
    password = PasswordField("", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField("Sign up", validators=[DataRequired()])


class SignInForm(FlaskForm):
    email = EmailField("", render_kw={"placeholder": "Email address"}, validators=[DataRequired(), Email()])
    password = PasswordField("", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField("Sign in", validators=[DataRequired()])


class TaskForm(FlaskForm):
    task = StringField("", render_kw={"placeholder": "Task"}, validators=[DataRequired()])
    category = SelectField("", render_kw={"placeholder": "Category"},
                           choices=["Foremost", "Crucial", "Important", "Minor"],
                           validators=[DataRequired()])
    date = DateField("", validators=[DataRequired()])
    submit = SubmitField("Add task", validators=[DataRequired()])


class DateForm(FlaskForm):
    date = DateField("", validators=[DataRequired()])
    submit = SubmitField("Select date", validators=[DataRequired()])


class UsernameForm(FlaskForm):
    username = StringField("", render_kw={"placeholder": "New username"}, validators=[DataRequired()])
    submit = SubmitField("Edit username", validators=[DataRequired()])
