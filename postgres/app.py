from flask import Flask, jsonify, make_response
from flask_migrate import Migrate 
from models import db, Customer
from dotenv import load_dotenv
from flask_restful import Resource, Api
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class Customers(Resource):

    def get(self):
        customers = [customer.to_dict() for customer in Customer.query.all()]
        return make_response(jsonify(customers), 200)


api.add_resource(Customers, '/customer')

class CustomerByID(Resource):

    def get(self, id):
        c = Customer.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(c), 200)

api.add_resource(CustomerByID, '/customer/<int:id>')


if __name__ == '__main__':
    app.run(port=5001, debug=True)






