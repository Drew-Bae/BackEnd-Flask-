from main import db, Student

db.create_all()

drew = Student('Drew', 100)
sam = Student('Sam', 105)

print(sam. id)
print(drew.id)

db.session.add_all([drew, sam])

db.session.commit()

print(drew.id)
print(sam.id)
