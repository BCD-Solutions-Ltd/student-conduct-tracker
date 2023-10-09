from App.models import Student
from App.database import db

def add_student(studentid, name):
    newstudent = Student(studentid=studentid, name=name)
    db.session.add(newstudent)
    db.session.commit()
    return student


def get_all_students():
    return Student.query.all()

def get_student(studentid):
    student = Student.query.filter_by(studentid=studentid).first()
    return student
    
def get_student_toJSON(studentid):
    student = StudentModel.query.filter_by(studentid=studentid).first()
    return student.toJSON()


def update_student(student_id, name):
    student = Student.query.get(student_id)
    if student:
        student.name = name
        print(student.name)
        db.session.commit(student)
        return db.session.commit()
    return None


