from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
app = Flask(__name__)
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "student"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,not_null=False)
    tests=db.relationship('TestMarks',backref="student")

class TestMarks(db.Model):
    __tablename__= "test_marks"
    id=db.Column(db.Integer, primary_key=True)
    test_name=db.Column(db.String,not_null=False)
    marks=db.Column(db.Integer,not_null=True)
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))



# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db.init_app(app)

# Create tables once
with app.app_context():
    db.create_all()

    # Insert sample data ONLY if DB is empty
    if Student.query.count() == 0:
        s1 = Student(name="Alice")
        s2 = Student(name="Bob")

        db.session.add_all([s1, s2])
        db.session.commit()

        t1 = TestMarks(test_name="Maths", marks=85, student_id=s1.id)
        t2 = TestMarks(test_name="Science", marks=92, student_id=s1.id)
        t3 = TestMarks(test_name="Maths", marks=78, student_id=s2.id)

        db.session.add_all([t1, t2, t3])
        db.session.commit()

@app.route("/")
def index():
    students = Student.query.filter_by(name="Priyanshu")
    print(students)
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)