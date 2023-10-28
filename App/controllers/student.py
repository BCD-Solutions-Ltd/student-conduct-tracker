from App.models import Student
from App.models import Review
from App.database import db
from json import dumps
from flask import jsonify


def create_student(stu_id, name):
    student = Student.query.get(stu_id)
    if student:
        return None
    new_student = Student(stu_id, name)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def update_student(stu_id, name):
    student = Student.query.get(stu_id)
    if student:
        student.name = name
        db.session.add(student)
        db.session.commit()
        return True

    return False

def search_student(stu_name):
    student = Student.query.filter_by(name=stu_name).first()
    if student:
        return student.to_json()
    return None

def get_all_students():
    students = Student.query.all()
    if not students:
        return []
    
    student_list = [student.to_json() for student in students]

    return student_list


def get_student(stu_id):
    student = Student.query.get(stu_id)
    return student

def calculate_karma(stu_id):
    student = Student.query.get(stu_id)
    if student:
        karma = sum([review.votes for review in student.reviews])
        student.karma = karma
        db.session.commit()
        return karma
    return None
