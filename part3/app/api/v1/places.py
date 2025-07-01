from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('places', description='Place operations')

review_output_model = api.model('ReviewOutput', {
    'id': fields.String,
    'text': fields.String,
    'rating': fields.Integer,
    'user_id': fields.String,
    'place_id': fields.String,
})

# Models
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

place_output_model = api.model('PlaceOutput', {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'latitude': fields.Float,
    'longitude': fields.Float,
})

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    @api.expect(place_model)
    @api.marshal_with(place_output_model, code=201)
    @api.response(400, 'Invalid input data.')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        owner_id = get_jwt_identity()
        if isinstance(owner_id, dict):
            owner_id = owner_id.get('id')
        user = facade.user_repo.get_by_attribute('id', owner_id)
        if not user:
            api.abort(400, 'Invalid input data.')
        try:
            place_data['owner_id'] = owner_id
            new_place = facade.create_place(place_data)
            return new_place, 201
        except Exception as e:
            api.abort(400, str(e))

    @api.marshal_with(place_output_model, as_list=True)
    @api.response(200, 'List of places retrieved successfully.')
    def get(self):
        """Retrieve a list of all places"""
        return facade.get_all_places(), 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.marshal_with(place_output_model)
    @api.response(200, 'Place details retrieved successfully.')
    @api.response(404, 'Place not found.')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Place not found.')
        return place, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully.')
    @api.response(404, 'Place not found.')
    @api.response(400, 'Invalid input data.')
    @api.response(403, 'Unauthorized action.')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Place not found.')
        current_user = get_jwt_identity()
        if isinstance(current_user, dict):
            current_user = current_user.get('id')
        if place["owner"]["id"] != current_user:
            api.abort(403, 'Unauthorized action.')
        try:
            facade.update_place(place_id, place_data)
            return {'message': 'Place updated successfully.'}, 200
        except Exception as e:
            api.abort(400, str(e))

@api.route('/<place_id>/amenities')
class PlaceAmenities(Resource):
    @jwt_required()
    @api.expect([amenity_model])
    @api.response(200, 'Amenities added successfully.')
    @api.response(404, 'Place not found.')
    @api.response(400, 'Invalid input data.')
    @api.response(403, 'Unauthorized action.')
    def post(self, place_id):
        current_user = get_jwt_identity()
        if isinstance(current_user, dict):
            current_user = current_user.get('id')
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Place not found.')
        if place["owner"]["id"] != current_user:
            api.abort(403, 'Unauthorized action.')
        amenities_data = api.payload
        if not amenities_data or len(amenities_data) == 0:
            api.abort(400, 'Invalid input data.')
        for amenity in amenities_data:
            a = facade.get_amenity(amenity['id'])
            if not a:
                api.abort(400, 'Invalid input data.')
        try:
            facade.add_amenities_to_place(place_id, amenities_data)
            return {'message': 'Amenities added successfully.'}, 200
        except Exception as e:
            api.abort(400, str(e))

@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.marshal_with(review_output_model, as_list=True)
    @api.response(200, 'List of reviews for the place retrieved successfully.')
    @api.response(404, 'Place not found.')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        try:
            return facade.get_reviews_by_place(place_id), 200
        except KeyError:
            api.abort(404, 'Place not found.')

