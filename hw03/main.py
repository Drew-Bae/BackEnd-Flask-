import os
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField)
from wtforms.validators import DataRequired, Optional
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hw03secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    grade = db.Column(db.Integer)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student {self.name} got {self.grade}. ID: {self.id}"


class InfoForm(FlaskForm):
    name1 = StringField('Enter the student\'s name',
                        validators=[DataRequired()])
    grade1 = IntegerField(
        'Enter the student\'s grade', validators=[DataRequired()])
    submit = SubmitField('enter')


class DisplayForm(FlaskForm):
    displayAll = SubmitField('List all students')


class DisplayPassForm(FlaskForm):
    displayPass = SubmitField('List the students who passed')


class DeleteForm(FlaskForm):
    studentID = StringField(
        'Enter the student\'s ID to delete: ', validators=[Optional()])
    delete = SubmitField('delete')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    form1 = DisplayForm()
    form2 = DisplayPassForm()
    form3 = DeleteForm()
    if form.validate_on_submit():
        session['name1'] = form.name1.data
        session['grade1'] = form.grade1.data
        new_student = Student(session['name1'], session['grade1'])
        db.session.add(new_student)
        db.session.commit()
        return render_template('home.html', form=form, form1=form1, form2=form2, form3=form3)
    elif form1.validate_on_submit():
        return redirect(url_for('results'))
    elif form2.validate_on_submit():
        return redirect(url_for('results'))
    elif form3.validate_on_submit():
        session['studentID'] = form3.studentID.data
        delete_student = Student.query.get(session['studentID'])
        db.session.delete(delete_student)
        db.session.commit()
        return render_template('home.html', form=form, form1=form1, form2=form2, form3=form3)
    return render_template('home.html', form=form, form1=form1, form2=form2, form3=form3)


@app.route('/results')
def results():
    all_students = Student.query.all()
    student_pass = Student.query.filter(Student.grade >= 85)
    return render_template('results.html', all_students=all_students, student_pass=student_pass)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
