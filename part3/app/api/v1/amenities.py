from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Enter 'Bearer' followed by your JWT token"
    }
}


api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

amenity_output_model = api.model('AmenityOutput', {
    'id':    fields.String(description='Amenity ID'),
    'name':  fields.String(description='Name of the amenity')
})


@api.route('/')
class AmenityList(Resource):
    @jwt_required()
    @api.doc(security='Bearer Auth')
    @api.marshal_with(amenity_output_model, code=201)
    @api.expect(amenity_model, validate=True)
    @api.response(201, 'Amenity successfully created.')
    @api.response(400, 'Invalid input data.')
    @api.response(403, 'Admin privileges required.')
    def post(self):
        """Register a new amenity"""
        claims = get_jwt()
        if not claims.get('is_admin'):
            api.abort(403, 'Admin privileges required.')
        amenity_data = api.payload

        name = amenity_data.get('name', '').strip()
        if not name:
            api.abort(400, 'Invalid input data.')
        amenity_data['name'] = name

        
        existing_amenity = facade.amenity_repo.get_by_attribute('name', amenity_data.get('name'))
        if existing_amenity:
            api.abort(400, 'error: Invalid input data.')
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return new_amenity, 201


        except Exception as e:
            api.abort(400, str(e))

    @api.marshal_list_with(amenity_output_model)
    @api.response(200, 'List of amenities retrieved successfully.')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return amenities, 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @jwt_required()
    @api.doc(security='Bearer Auth')
    @api.marshal_with(amenity_output_model)
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found')
        return amenity, 200

    @api.expect(amenity_model, validate=True)
    @api.marshal_with(amenity_output_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required.')
    @jwt_required()
    @api.doc(security='Bearer Auth')
    def put(self, amenity_id):
        claims = get_jwt()
        if not claims.get('is_admin'):
            api.abort(403, 'Admin privileges required')

        amenity_data = api.payload

        name = amenity_data.get('name', '').strip()
        if not name:
            api.abort(400, 'Invalid input data.')
        amenity_data['name'] = name


        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found')

        existing_amenity = facade.amenity_repo.get_by_attribute('name', amenity_data.get('name'))
        if existing_amenity and existing_amenity.id != amenity_id:
            api.abort(400, 'Amenity with this name already exists')
        try:
            updated =facade.update_amenity(amenity_id, amenity_data)
            return updated, 200
        except Exception as e:
            api.abort(400, str(e))

