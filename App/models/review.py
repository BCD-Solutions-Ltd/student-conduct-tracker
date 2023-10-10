from json import dumps
from App.database import db
from dataclasses import dataclass

@dataclass
class Review(db.Model):
    rev_id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('student.stu_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)

    def __init__(self,rev_id, stu_id, message):
        self.rev_id = rev_id
        self.stu_id = stu_id
        self.content = message

    def __repr__(self):
        return f'<{self.rev_id}| {self.stu_id} {self.content} -- {self.votes}>'

    def to_json(self):
        review_json = {
            'review ID' : self.rev_id,
            'student Id' : self.stu_id,
            'Review Text': self.content,
            'Votes': self.votes
        }
        return dumps(review_json)
