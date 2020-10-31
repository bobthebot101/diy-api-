from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

class helloworld(Resource):
    def get(self, name):
        return {"data": name}
    
api.add_resource(helloworld, '/helloworld/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)


 
