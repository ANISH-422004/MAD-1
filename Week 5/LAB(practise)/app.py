from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy(app) 


class Student(db.Model): 
    __tablename__ = 'student'
    student_id = db.Column(db.Integer() , primary_key = True , autoincrement = True)
    roll_number = db.Column(db.String(20), nullable = False , unique = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50))
    courses = db.relationship('Course' , backref="student" , secondary = 'enrollments' , lazy='dynamic' )

#<Student 1> -- > { student_id : 1 , roll_number : "CSE2021001" , first_name : "John" , last_name : "Doe" , courses : [<Course 1> , <Course 2> ] }

class Course(db.Model): 
    __tablename__ = 'course'
    course_id = db.Column(db.Integer() , primary_key = True , autoincrement = True)
    course_code = db.Column(db.String(20), nullable = False , unique = True)
    course_name = db.Column(db.String(100), nullable = False)
    course_description = db.Column(db.Text())
    
# <Course 1> -- > { course_id : 1 , course_code : "CSE01" , course_name : "MAD I" , course_description : "Modern Application Development - I" }

class Enrollments(db.Model):
    __tablename__ = 'enrollments' 
    enrollment_id  = db.Column(db.Integer() , primary_key = True , autoincrement = True )
    estudent_id = db.Column(db.Integer() , db.ForeignKey('student.student_id') , nullable = False)
    ecourse_id = db.Column(db.Integer() , db.ForeignKey('course.course_id') , nullable = False)
   
    
    
with app.app_context() :
    # courses_data = [
    #     ("CSE01", "MAD I", "Modern Application Development - I"),
    #     ("CSE02", "DBMS", "Database Management Systems"),
    #     ("CSE03", "PDSA", "Programming, Data Structures and Algorithms using Python"),
    #     ("BST13", "BDM", "Business Data Management")
    # ]
    # Course.add_all([Course(course_code=code, course_name=name, course_description=desc) for code, name, desc in courses_data])
    db.create_all()
    
    
@app.route('/')
def index():
    students = Student.query.order_by(Student.roll_number).all()
    if not students:
        return render_template("index_alt.html")
    return render_template('index.html' , students=students)

@app.route('/student/create' , methods = ['GET','POST'])
def create_student(): 
     if request.method == 'GET': 
        return render_template('create.html')
     if request.method == 'POST': 
        roll = request.form.get("roll")
        f_name = request.form.get("f_name")
        l_name = request.form.get("l_name")
        courses = request.form.getlist("courses") # getlist is a method which is used to get multiple values from a form input with the same name attribute.   
        
        
        exsisting_student = Student.query.filter_by(roll_number=roll).first()
        if exsisting_student:
            return "Student with this roll number already exists!"
        
        new_student = Student(roll_number=roll , first_name=f_name , last_name=l_name)
        db.session.add(new_student)
        db.session.commit()
        
        
        # now we need to update enrollments table to add the courses for this student.
        for c in courses:
            s_id = new_student.student_id
            new_e = Enrollments(estudent_id = s_id , ecourse_id = int(c[-1])  )
            db.session.add(new_e)
            
            db.session.commit()
        
        return redirect('/')
        
if __name__ == '__main__':
    app.run(debug=True , port=5000)
    