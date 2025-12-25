from flask import Flask , render_template
from db.db import db
from config.config import Config
from models.models import *

app = Flask(__name__ , template_folder="templates" , static_folder="static")

app.config.from_object(Config)
db.init_app(app)


with app.app_context():
    db.create_all()
    admin = Role.query.filter_by(name="admin").first()
    if not admin:
        admin_role  = Role(name = "admin")
        db.session.add(admin_role)
        db.session.commit()
        
    customer = Role.query.filter_by(name="customer").first()
    if not customer:
        customer_role  = Role(name = "customer")
        db.session.add(customer_role)
        db.session.commit()
        
    manager = Role.query.filter_by(name="manager").first()
    if not manager:
        manager_role  = Role(name = "manager")
        db.session.add(manager_role)
        db.session.commit()
        

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/about")
def about():
    return "This is a simple Flask application."



if __name__ == "__main__":
    app.run(debug=True)
    
