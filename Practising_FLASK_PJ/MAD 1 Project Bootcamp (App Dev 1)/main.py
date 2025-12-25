from flask import Flask, render_template
from db.db import db
from config.config import Config
from models.models import *

app = Flask(__name__, template_folder="templates", static_folder="static")

app.config.from_object(Config)
db.init_app(app)


with app.app_context():
    # 1️⃣ Create tables
    db.create_all()

    # 2️⃣ Create roles if not exists
    roles = ["admin", "customer", "manager"]

    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            db.session.add(Role(name=role_name))

    db.session.commit()

    # 3️⃣ Create Super Admin user
    admin_user = User.query.filter_by(email="admin@gmail.com").first()

    print(admin_user.roles)

    if not admin_user:
        
        admin_role_id = Role.query.filter_by(name="admin").first()
        admin_user = User(
            name="Super_Admin",
            email="admin@gmail.com",
            password="admin",
            roles=[admin_role_id]
        )
        db.session.add(admin_user)
        db.session.commit()  # user_id generated here

        



    # 4️⃣ Assign admin role to Super Admin
    





@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return "This is a simple Flask application."


if __name__ == "__main__":
    app.run(debug=True)
