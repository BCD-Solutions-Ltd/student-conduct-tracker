from App.models import Student
from App.models import Review
from App.database import db

def log_review(studentid, review_t):
    student = Student.query.get(studentid)
    if student:
        review = Review(review_t=review_t, student=student)
        db.session.add(review)
        db.session.commit()
        return review
    return None


def upvote_review(revid):
    review = Review.query.get(revid)
    if review:
        review.upvotes += 1
        db.session.commit()
        return review

def downvote_review(revid):
    review = Review.query.get(revid)
    if review:
        review.downvotes += 1
        db.session.commit()
        return review




