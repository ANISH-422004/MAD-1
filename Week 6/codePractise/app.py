from flask import Flask, request
from flask_restful import Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)
api = Api(app)  
# Why Api(app)?
# → Replaces @app.route
# → Manages routing for REST resources


# =========================
# Models
# =========================
class EmployeeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    salery = db.Column(db.Float(precision=2))


with app.app_context():
    db.create_all()


# =========================
# Serialization fields
# =========================
employee_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "salery": fields.Float,
}


# =========================
# Controllers
# =========================
# 🔹 What is Resource?
# A class-based route
class EmployeeController(Resource):
    # Resource is a base class that you inherit to create REST API endpoints
    # just like db.Model

    @marshal_with(employee_fields)
    def get(self, id):
       
        e = EmployeeModel.query.get(id)
        # ❌ This is a SQLAlchemy object, not JSON
        # Flask-RESTful does NOT know how to convert it cleanly
        # Therefore we need to serialize it
        # DB object → marshaled → JSON response
        
        
        if e is None:
            print("Employee not found")
            return {"message": "Employee not found"}, 404

        return e , 200 # marshal_with automatically converts it

    @marshal_with(employee_fields)
    def post(self):
        data = request.get_json() # reads request body - > parses JSON -> python dict
        print(data)
        # Handle case: invalid or missing data
        if( not data) or ("name" not in data) or ("salery" not in data):
            return {"message": "Invalid input data"}, 400

        new_employee = EmployeeModel(
            name=data["name"],
            salery=data["salery"],
        )

        try:
            db.session.add(new_employee)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # if db error happens, rollback can be done here
            return {"message": "Database error"}, 500

        return {"message": "Employee added successfully" , "employee": new_employee}, 201


    def put(self, id):
        e = EmployeeModel.query.get(id)

        # Handle case: employee not created in DB
        if e is None:
            return {"message": "Employee not found"}, 404

        data = request.get_json()

        if "name" in data:
            e.name = data["name"]
        if "salery" in data:
            e.salery = data["salery"]
    
        try : 
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "ISE : please try again later"}, 500

        return {"message": "Employee updated successfully"}, 200


    def delete(self, id):
        e = EmployeeModel.query.get(id)

        # Handle case: employee not created in DB
        if e is None:
            return {"message": "Employee not found"}, 404

        db.session.delete(e)
        try : 
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": "ISE : please try again later"}, 500
        
        
        return {"message": "Employee deleted successfully"}, 200


# =========================
# Routing  :: Adding Resource to the API
# =========================
api.add_resource(
    EmployeeController,
    "/employee",
    "/employee/<int:id>"
)
# Why add_resource?
# → To bind Resource to a route


if __name__ == "__main__":
    app.run(debug=True)
