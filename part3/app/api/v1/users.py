from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_bcrypt import Bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

bcrypt = Bcrypt()

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='User password'),
    
})

user_output_model = api.model('UserOutput', {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.marshal_with(user_output_model, code=201)
    @api.response(409, 'Email already registered.')
    @api.response(400, 'Invalid input data.')
    @api.response(403, 'Admin privileges required.')
    @jwt_required()
    def post(self):
        """Register a new user by admin"""
        user_data = api.payload
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            api.abort(409, 'Email already registered.')

        all_users = facade.get_users()
        if not all_users:
            user_data['is_admin'] = True
        else:
            user_data['is_admin'] = False
  
        user_data['password'] = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        try:
            new_user = facade.create_user(user_data)
            return new_user, 201
        except Exception as e:
            api.abort(400, str(e))

    @api.marshal_with(user_output_model, as_list=True)
    @api.response(200, 'List of users retrieved successfully.')
    def get(self):
        """Retrieve a list of users"""
        users = facade.get_users()
        return users, 200

@api.route('/<user_id>')
class UserResource(Resource):
    @jwt_required()
    @api.marshal_with(user_output_model)
    @api.response(200, 'User details retrieved successfully.')
    @api.response(404, 'User not found.')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found.')
        return user, 200

    @jwt_required()
    @api.expect(user_model)
    @api.marshal_with(user_output_model)
    @api.response(200, 'User updated successfully.')
    @api.response(404, 'User not found.')
    @api.response(400, 'Invalid input data.')
    @api.response(403, 'Admin privileges required.')
    def put(self, user_id):
        claims = get_jwt()
        if not claims.get("is_admin"):
            api.abort(403, "Admin privileges required.")

        user_data = api.payload
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found.')

        for field in ['first_name', 'last_name', 'email', 'password']:
            if field in user_data and not user_data[field].strip():
                api.abort(400, f"{field.replace('_', ' ').capitalize()} cannot be empty.")


        email = user_data.get('email')
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                api.abort(409, 'Email already registered.')

        password = user_data.get('password')
        if password:
            user_data['password'] = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            facade.update_user(user_id, user_data)
            updated_user = facade.get_user(user_id)
            return updated_user, 200
        except Exception as e:
            api.abort(400, str(e))
