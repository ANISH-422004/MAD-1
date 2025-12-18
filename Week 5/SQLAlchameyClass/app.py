from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Step 1: Initialize Flask app
app = Flask(__name__)

# Step 2: Configure SQLAlchemy database URI
# 'sqlite:///test.db' → relative path (inside instance folder)
# Flask automatically uses the "instance/" folder for SQLite databases
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Step 3: Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app) # db is an SQLAlchemy helper object that acts as a bridge between Flask and SQLAlchemy.

# Step 4: Define a database model (a table in SQL)
class User(db.Model):  #class --> Table and db.Model is a base class for all models from SQLAlchemy meaning User is a table in the database 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # String representation (useful for debugging)
    def __repr__(self):
        return f"<User {self.username}>"

# Step 5: Create all database tables inside the app context  
with app.app_context(): ## Ensure we are in the app context to create tables why ? Because Flask-SQLAlchemy needs the application context to access configuration and other app-specific data.
        # ''with'' keyword in Python is used to work with context managers.
        # ''with'' keyword in Python is used to work with context(A context is a controlled scope in which resources are acquired and released automatically.) managers.
        
        
                                        # Context manager (with statement) Exmaple :::: 
                                        # with open("data.txt") as f:
                                        #     data = f.read()
                                        # # file is automatically closed here


                                        # Here:

                                        # Enter context → file is opened

                                        # Exit context → file is closed (even if an error happens)
                                        
        
        
        # A context manager sets something up before the block runs and cleans it up after the block exits — automatically, even if an error happens.
    
    db.create_all() ## Create the database tables if they don't exist and if they exist then it will not create again 

# Step 6: Define routes
@app.route("/")
def index():
    users = User.query.all() # Fetch all users from the database in Python_List of Python_Object  [<User ucigrsxr>, <User dqbcejku>]
    print(users)  # Debugging: print the list of users to the console
    return render_template("index.html", users=users)

@app.route("/addrandomuser")
def add_random_user():
    import random
    import string

    # Generate random username and email
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    email = f"{username}@example.com"

    # Create a new User instance
    new_user = User(username=username, email=email) # Create a new user instance Python_Object
    
    # Add the new user to the database
    db.session.add(new_user)
    
    # Commit the changes
    db.session.commit()
    
    return redirect(url_for('index'))

# Step 7: Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
