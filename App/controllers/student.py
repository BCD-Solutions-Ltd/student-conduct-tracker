from App.models import Student
from App.database import db

def add_student(name):
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    return student


def update_student(student_id, name):
    student = Student.query.get(student_id)
    if student:
        student.name = name
        db.session.commit(student)
        return db.session.commit()
    return None

def get_all_students():
    return Student.query.all()

