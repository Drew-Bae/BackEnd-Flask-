import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, IntegerField, SubmitField)
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hw04secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class YellowPages(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.Text)
    email = db.Column(db.Text)
    phoneNumber = db.Column(db.Integer)
    address = db.Column(db.Text)

    def __init__(self, companyName, email, phoneNumber, address):
        self.companyName = companyName
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address

    def __repr__(self):
        return f"Company Name: {self.companyName}  |  Email: {self.email}  |  Phone Number: {self.phoneNumber}  |  Address: {self.address}"


class Form(FlaskForm):
    companyName = StringField('Company Name', render_kw={
                              "placeholder": "Company Name"})
    email = EmailField('Email', render_kw={
                       "placeholder": "somename@gmail.com"})
    phoneNumber = IntegerField('Phone Number', render_kw={
                               "placeholder": "2052665355"})
    address = StringField('Address', render_kw={
                          "placeholder": "11 Some St. 35222 Hoover, Al"})
    submit = SubmitField('Register')


class Delete(FlaskForm):
    phoneNumber = IntegerField('Phone Number', render_kw={
                               "placeholder": "2052665355"})
    submit = SubmitField('Delete')


@app.route('/', methods=['GET', 'POST'])
def main():
    form = Form()
    Users = YellowPages.query.all()
    if form.validate_on_submit():
        session['companyName'] = form.companyName.data
        session['email'] = form.email.data
        session['phoneNumber'] = form.phoneNumber.data
        session['address'] = form.address.data
        db.session.add(YellowPages(
            session['companyName'], session['email'], session['phoneNumber'], session['address']))
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('main.html', form=form, Users=Users)


@app.route('/base.html', methods=['GET', 'POST'])
def delete():
    form1 = Delete()
    if form1.validate_on_submit():
        session['delete_phoneNumber'] = form1.phoneNumber.data
        delete = YellowPages.query.filter_by(
            phoneNumber=session['delete_phoneNumber']).first()
        delete1 = YellowPages.query.get(delete.id)
        db.session.delete(delete1)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('base.html', form1=form1)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
