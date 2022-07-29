from crypt import methods
from distutils.log import debug
import os
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lab08secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

    # def __repr__(self): (don't need?)


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    login = SubmitField('Login')


class SignUpForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirmPassword = StringField(
        'Confirm Password', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        # something to test with database (grab data from db)
        # if match with db then return bottom (else message)
        return render_template('secretPage.html', form=form)


@app.route('/signup')
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        session['firstName'] = form.firstName.data
        session['lastName'] = form.lastName.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        session['confirmPassword'] = form.confirmPassword.data
        # add data in db by (db.session.add/commit)
        return render_template('secretPage.html', form=form)


if __name__ == '__main___':
    db.create_all()
    app.run(debug=True)
