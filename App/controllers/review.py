from App.models import Student
from App.models import Review
from App.database import db
from json import dumps

def create_review(rev_id, stu_id, content):
    student = Student.query.get(stu_id)
    if student:
        review = Review(rev_id, stu_id, content)
        db.session.add(review)
        db.session.commit()
        return review
    return None

def list_reviews():
    return Review.query.all()

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

def find_review_by_id(revid):
    review = Review.query.get(revid)
    return dumps(review)

