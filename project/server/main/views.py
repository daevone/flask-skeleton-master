# project/server/main/views.py

from mayan_api_client import API

from flask import render_template, Blueprint

from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField
from wtforms.validators import DataRequired


main_blueprint = Blueprint('main', __name__,)

api = API(host='http://192.168.22.188:81', username='Dave', password='dbvjdu123')

class SomeForm(FlaskForm):

    invoice_number = StringField('Invoice number (Required)', [DataRequired()])
    test = SelectField('test', choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004)], \
                       validators=[DataRequired()])
    status = SelectField('status', choices=[('nova', 'nova'), ('zauctovano', 'zauctovano')])

@main_blueprint.route('/')
def home():
    form = SomeForm()
    return render_template('main/home.html', form=form)


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
