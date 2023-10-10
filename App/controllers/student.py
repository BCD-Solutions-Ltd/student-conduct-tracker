from App.models import Student
from App.models import Review
from App.database import db


def create_student(stu_id, name):
    student = Student(stu_id, name)
    db.session.add(student)
    db.session.commit()
    return student

def update_student(stu_id, name):
    student = Student.query.get(stu_id)
    if student:
        student.name = name
        db.session.add(student)
        db.session.commit()
        return

    return None

def search_student(stu_name):
    student = Student.query.filter_by(name=stu_name).first()
    if student:
        return student.to_json()
    return None

def get_all_students():
    return Student.query.all()

def get_student(stu_id):
    student = Student.query.get(stu_id)
    return student

# def calculate_karma(stu_id):
#     student = Student.query.get(stu_id)
#     if student:
#         karma = sum([review.upvotes - review.downvotes for review in student.reviews])
#         student.karma = karma
#         db.session.commit()
#         return student
#     return None
