from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

students = []

class Student(Resource):
    def get(self, student_id):
        print(students)
        for student in students:
            if student["id"] == student_id:
                return jsonify(student)
        return jsonify({"message": "Student not found"}), 404

    def post(self, student_id):
        data = request.get_json()
        new_student = {
            "id": data["id"],
            "name": data["name"]
        }
        students.append(new_student)
        print(students)
        return jsonify({"message": "Student added successfully"})

api.add_resource(Student, "/student" ,"/student/<int:student_id>")

if __name__ == '__main__':
    app.run(debug=True)
