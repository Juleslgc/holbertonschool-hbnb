from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.models import amenity


api = Namespace('amenities', description='Amenity operations')


# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})


@api.route('/')
class AmenityList(Resource):
    """
    Handles listing and creation of amenities.
    """
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new amenity
        """
        amenity_data = api.payload
        try:
            amenity = facade.create_amenity(amenity_data)
            return {'id': amenity.id, 'name': amenity.name}, 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """
        Retrieve a list of all amenities
        """
        amenities = facade.get_all_amenities()
        return amenities, 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    """
    Handles retrieval, update, and deletion of a specific amenity.
    """
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """
        Get amenity details by ID
        """
        try:
            amenity = facade.get_amenity(amenity_id)
            return amenity.to_dict(), 200
        except Exception as e:
            return {'error': str(e)}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """
        Update an amenity's information
        """
        amenity_data = api.payload
        before_amenity = facade.get_amenity(amenity_id)
        if before_amenity is None:
            return {'error': 'Amenity not found'}, 404
        try:
            update_amenity = facade.update_amenity(amenity_id, amenity_data)
            return {"message": "Amenity updated successfully"}, 200
        except Exception as e:
            return {'error': str(e)}, 400