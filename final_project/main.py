import os
from urllib import request
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField,
                     SearchField, SelectMultipleField)
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'finalprojectsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Some Text Inside Class User"


class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={
                           "placeholder": "Username"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             "placeholder": "Password"})
    login = SubmitField('Login')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={
                           "placeholder": "Username"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             "placeholder": "Password"})
    confirmPassword = PasswordField("Confirm Password", validators=[
                                    DataRequired()], render_kw={"placeholder": "Confirm Password"})
    register = SubmitField('Register Now')


@app.route('/', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['password'] = form.password.data
        test = User.query.filter_by(username=session['username']).first()
        if test == None:
            return redirect(url_for('signin'))
        elif test.password == session['password']:
            return render_template('main.html', form=form)
        else:
            return redirect(url_for('signin'))
    return render_template('signIn.html', form=form)


@app.route('/signUp.html', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['confirmPassword'] = form.confirmPassword.data
        new_user = User(session['username'], session['password'])
        test = User.query.filter_by(username=session['username']).first()
        if test != None:
            return redirect(url_for('signup'))
        elif session['password'] != session['confirmPassword']:
            return redirect(url_for('signup'))
        else:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('signin'))
    return render_template('signUp.html', form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
