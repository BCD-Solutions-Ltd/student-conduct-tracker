# controllers.py
from flask import jsonify
from App.models import db, Student, Review

def add_student(name):
    student = Student(name)
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student successfully added"})

def update_student(student_id, new_name):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "This student was not found"}), 404

    student.name = new_name
    db.session.commit()
    return jsonify({"message": "Student successfully updated"})

def log_review(student_id, review_t):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "This student was not found"}), 404

    review = Review(student_id=student_id, review_text=review_t)
    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "Review was sent successfully"})

def search_student(name):
    students = Student.query.filter(Student.name.ilike(f"%{name}%")).all()
    if not students:
        return jsonify({"message": "This student was not  found"})

    result = [{"id": student.id, "name": student.name, "karma_score": student.karma_score} for student in students]
    return jsonify(result)
