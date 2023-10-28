from json import dumps
from App.database import db
from dataclasses import dataclass

@dataclass
class Student(db.Model):
    stu_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    karma = db.Column(db.Integer, default=0)
    reviews = db.relationship('Review', backref='student', lazy=True)

    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def __repr__(self):
        return f'<{self.stu_id} | {self.name} -- {self.karma}>'

    def to_json(self):
        student_json = {
            'student ID' : self.stu_id,
            'student Name' : self.name,
            'karma': self.karma,
            'reviews': [review.to_json() for review in self.reviews]
        }
        return student_json
