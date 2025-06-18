#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.models.user import User

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True),
})
user_put_model = api.model('UserPut', {
    'email': fields.String(required=False),
    'first_name': fields.String(required=False),
    'last_name': fields.String(required=False),
    'password': fields.String(required=False),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered or invalid input')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        
        if not User.verified_email(user_data['email']):
            return {'error': 'Invalid email format'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email, 'created_at': new_user.created_at.isoformat()}, 201

    @api.response(200, 'List of users successfully retrieved')
    def get(self):
        """
        retrieve list of all users
        """
        users = facade.get_all_users()
        return users, 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_put_model, validate=True)
    @api.response(200, 'User is successfully retrieved')
    @api.response(404, 'User does not exist')
    @api.response(400, 'Email already registered')
    def put(self, user_id):
        data = api.payload
        user = facade.get_user(user_id)
        if user is None:
            return {"error": "User not found"}, 404

        try:
            existing_user = facade.get_user_by_email(data['email'])
            if existing_user and existing_user != user:
                return {"error": "Email already registered"}, 400
        
            if not User.verified_email(data['email']):
                return {'error': 'Invalid email format'}, 400

            updated_user = facade.update(user_id, data)
            if updated_user is None:
                return {'error': 'Updates failed'}
            return updated_user.to_dict(), 200
        except Exception as e:
            return {'error': str(e)}, 400