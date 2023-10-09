from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    review_t = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    next_id = 1

    def __init__(self, student_id, content):
        self.id = Review.next_id
        self.student_id = student_id
        self.review_t = content
        Review.next_id += 1

    def __repr__(self):
        return f'{self.id} Review of {self.student_id}: {self.review_t}'
    
    def upvote(self):
        self.votes += 1

    def downvote(self):
        self.votes -= 1

    def toJson():
        return{
            "review ID" : self.revid,
            "student Id" : self.studentid,
            " Review ": self.review_t
        }
