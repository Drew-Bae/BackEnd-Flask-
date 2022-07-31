import os
from urllib import request
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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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

    def __repr__(self):
        return f"Some text."


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired()], render_kw={"placeholder": "Email"})
    password = StringField('Password', validators=[DataRequired()], render_kw={
                           "placeholder": "Password"})
    login = SubmitField('Login')


class SignUpForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()], render_kw={
                            "placeholder": "First Name"})
    lastName = StringField('Last Name', validators=[DataRequired()], render_kw={
                           "placeholder": "Last Name"})
    email = StringField('Email', validators=[DataRequired()], render_kw={
                        "placeholder": "Email"})
    password = StringField('Password', validators=[DataRequired()], render_kw={
                           "placeholder": "Password"})
    confirmPassword = StringField(
        'Confirm Password', validators=[DataRequired()], render_kw={"placeholder": "Confirm Password"})
    register = SubmitField('Register Now')


@app.route('/', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        test = User.query.filter_by(email=session['email']).first()
        if test.password == session['password']:
            return render_template('secretPage.html', form=form)
    return render_template('signInPage.html', form=form)


@app.route('/signUpPage.html', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    error = None
    if form.validate_on_submit():
        session['firstName'] = form.firstName.data
        session['lastName'] = form.lastName.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        session['confirmPassword'] = form.confirmPassword.data
        new_user = User(session['firstName'], session['lastName'],
                        session['email'], session['password'])
        if session['password'] != session['confirmPassword']:
            error = 'Password does not match'
        else:
            new_user = User(session['firstName'], session['lastName'],
                            session['email'], session['password'])
            db.session.add(new_user)
            db.session.commit()
            return render_template('thankYou.html', form=form)
    return render_template('signUpPage.html', form=form, error=error)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
