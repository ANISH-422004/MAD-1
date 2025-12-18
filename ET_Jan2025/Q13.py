from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class MyApi(Resource):
    def get(self):
        return {"message":"Hello user!"}

    def put(self):
        return {"message":"Hello World!"}
    def post(self):
        return {"message": "post method"}

api.add_resource(MyApi, '/api/get','/api/put', '/api/post')

app.run()