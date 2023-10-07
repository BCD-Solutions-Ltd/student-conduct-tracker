from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Reviews', backref='student', lazy=True)
    karma = db.Column(db.Integer, default=0)
    next_id = 1

    def __init__(self, student_name):
        self.id = Student.next_id
        self.name = student_name
        Student.next_id += 1

    def __repr__(self):
        return f'<Student {self.id} {self.name} - {self.karma} Karma'

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
    