from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
api = Api(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    created_by = db.Column(db.Integer)
    modified_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    modified_by = db.Column(db.Integer)
    is_deleted = db.Column(db.Boolean, default=False)

    def __init__(self, name, email, phone_number, address, is_admin, username, password, created_by, modified_by):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.is_admin = is_admin
        self.username = username
        self.password = password
        self.created_by = created_by
        self.modified_by = modified_by

# Create the database schema
db.create_all()

# Request parser for updating username and password
update_parser = reqparse.RequestParser()
update_parser.add_argument('username', type=str)
update_parser.add_argument('password', type=str)

# User resource
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone_number': user.phone_number,
                'address': user.address,
                'is_admin': user.is_admin,
                'username': user.username,
                'password': user.password,
                'created_at': user.created_at,
                'created_by': user.created_by,
                'modified_at': user.modified_at,
                'modified_by': user.modified_by,
                'is_deleted': user.is_deleted
            }
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        args = update_parser.parse_args()
        user = User.query.get(user_id)
        if user:
            if args['username']:
                user.username = args['username']
            if args['password']:
                user.password = args['password']
            db.session.commit()
            return {'message': 'Username and/or password updated successfully'}
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            user.is_deleted = True
            db.session.commit()
            return {'message': 'User deleted successfully'}
        return {'message': 'User not found'}, 404

# Users resource
class UsersResource(Resource):
    def get(self):
        users = User.query.filter_by(is_deleted=False).all()
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone_number': user.phone_number,
                'address': user.address,
                'is_admin': user.is_admin,
                'username': user.username,
                'password': user.password,
                'created_at': user.created_at,
                'created_by': user.created_by,
                'modified_at': user.modified_at,
                'modified_by': user.modified_by,
                'is_deleted': user.is_deleted
            })
        return {'users': user_list}

    def post(self):
        args = request.get_json()
        user = User(**args)
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(UsersResource, '/users')

if __name__ == '__main__':
    app.run(debug=True)
