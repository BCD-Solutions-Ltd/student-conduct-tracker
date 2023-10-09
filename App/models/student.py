from App.database import db

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


    def toJson():
        return{
            "student ID" : self.studentid,
            "student Name" : self.name
        }
    
    
