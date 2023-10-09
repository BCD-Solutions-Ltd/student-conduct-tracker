from App.database import db

class Review(db.Model):
    revid = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.studentid'), nullable=False)
    review_t = db.Column(db.Text, nullable=False)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

def toJson():
    return{
        "review ID" : self.revid,
        "student Id" : self.studentid,
        " Review Text ": self.review_t
        'upvotes': self.upvotes,
        'downvotes': self.downvotes,  
    }
