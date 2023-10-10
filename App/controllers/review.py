from App.models import Student
from App.models import Review
from App.database import db

def create_review(stu_id, content):
    student = Student.query.get(stu_id)
    if student:
        review = Review(stu_id, content)
        db.session.add(review)
        db.session.commit()
        return review
    return None

def list_reviews():
    reviews = Review.query.all()
    return reviews

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




