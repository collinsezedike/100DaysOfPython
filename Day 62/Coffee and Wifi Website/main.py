from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap(app)


def create_choices_list(label, other_options: list):
    choices_list = [label]
    for items in other_options:
        choices_list.append(items)
    return choices_list


class CafeForm(FlaskForm):

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=["☕" * num for num in range(6) if num != 0],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating',
                              choices=create_choices_list("✘", ["💪"*num for num in range(6) if num != 0]),
                              validators=[DataRequired()])
    power_outlet = SelectField('Power Socket Availability',
                               choices=create_choices_list("✘", ["🔌"*num for num in range(6) if num != 0]),
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        submitted_data = [form.cafe.data, form.location.data, form.opening_time.data, form.closing_time.data,
                          form.coffee_rating.data, form.wifi_rating.data, form.power_outlet.data]
        with open("cafe-data.csv", "a", newline='', encoding="utf8") as csv_File:
            writer = csv.writer(csv_File)
            writer.writerow(submitted_data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open("cafe-data.csv", newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
