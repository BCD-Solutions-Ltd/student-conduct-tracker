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
    reviews = Review.query.all()
    if not reviews:
        return []
    
    review_list = [review.to_json() for review in reviews]

    return review_list

def upvote_review(stu_id, rev_id):
    student = Student.query.get(stu_id)
    if student:
        review = Review.query.filter_by(rev_id=rev_id).first()
        if review:
            review.votes += 1
            db.session.commit()
            return review
        return None
        
    return None

def downvote_review(stu_id, rev_id):
    student = Student.query.get(stu_id)
    if student:
        review = Review.query.filter_by(rev_id=rev_id).first()
        if review:
            review.votes -= 1
            db.session.commit()
            return review
        return None
        
    return None

def find_review_by_id(rev_id):
    review = Review.query.get(rev_id)
    return review

