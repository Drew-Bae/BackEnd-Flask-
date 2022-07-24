from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lab7secretkey'


class InfoForm(FlaskForm):
    username = StringField('UserName: ', validators=[DataRequired()])
    password = StringField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Submit Form')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['password'] = form.password.data
        return redirect(url_for('info'))

    return render_template('index.html', form=form)


@app.route('/report')
def info():
    passes = "Your Password passed the 3 requirements!"
    failed = "Here are the requirments you failed:"
    failedUpper = "You did not have a uppercase character"
    failedLower = "You did not have a lowercase character"
    failedNumber = "You did not have a number at the end"
    return render_template('report.html', passes=passes, failed=failed, failedUpper=failedUpper, failedLower=failedLower, failedNumber=failedNumber)


if __name__ == '__main__':
    app.run(debug=True)
