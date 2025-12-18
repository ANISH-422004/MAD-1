from flask import Flask , render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

'''
Flask-SQLAlchemy does NOT come with its own database.
It simply gives you an ORM layer on top of whatever database you choose.
'''
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/mydb'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"

db = SQLAlchemy(app) ## Initializing the SQLAlchemy object with the Flask app , thginf this db as a handle to interact with the database

class Post(db.Model): 
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(100) , nullable = False)
    content = db.Column(db.Text , nullable = False)
    
    
with app.app_context():
    db.create_all()  ## Create the database tables if they do not exist already otherwise it will do nothing




@app.route("/")
def index():
    db_posts = Post.query.all()
    print(db_posts)
    return render_template("index.html" , posts = db_posts)

@app.route("/add_post" , methods = ["GET" , "POST"])
def add_post(): 
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        new_post = Post(title = title , content = content)
        db.session.add(new_post) ## Adding the new post to the current database session
        db.session.commit()  ## Committing the changes to the database
        return  redirect ("/")
    if request.method == "GET":
        return render_template("add_post.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)
    