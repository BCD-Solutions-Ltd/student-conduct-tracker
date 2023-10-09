from App.database import db

class Review(db.Model):
    revid = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    review_t = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    

def toJson():
    return{
        "review ID" : self.revid,
        "student Id" : self.studentid,
        " Review ": self.review_t
    }
