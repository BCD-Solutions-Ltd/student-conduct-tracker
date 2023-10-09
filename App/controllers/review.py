from App.models import Student
from App.models import Review
from App.database import db

def log_review(student_id, content):
    student = Student.query.get(student_id)
    if student:
        review = Review(content=content, student=student)
        db.session.add(review)
        db.session.commit()
        return review
    return None


def upvote_review(review_id):
    review = Review.query.get(review_id)
    if review:
        review.upvotes += 1
        db.session.commit()
        return review

def downvote_review(review_id):
    review = Review.query.get(review_id)
    if review:
        review.downvotes += 1
        db.session.commit()
        return review

def calculate_karma(student_id):
    student = Student.query.get(student_id)
    if student:
        karma = sum([review.upvotes - review.downvotes for review in student.reviews])
        student.karma = karma
        db.session.commit()
        return student
    return None



