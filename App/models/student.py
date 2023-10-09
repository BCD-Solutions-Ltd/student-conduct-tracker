from App.database import db

class Student(db.Model):
    studentid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    karma = db.Column(db.Integer, default=0)

def toJson():
    return{
        "student ID" : self.studentid,
        "student Name" : self.name
        'karma': self.karma, 
    }
    

