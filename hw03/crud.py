from main import db, Student, home

new_student = Student(home(form.name1.data), home(form.grade1.data))
db.session.add(new_student)
db.session.commit()

all_students = Student.query.all()

student_pass = Student.query.filter(Student.grade >= 85)

print(all_students)
