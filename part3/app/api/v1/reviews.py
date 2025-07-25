from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
})

review_output_model = api.model('ReviewOutput', {
    'id': fields.String,
    'text': fields.String,
    'rating': fields.Integer,
    'place_id': fields.String,
    'user_id': fields.String
})

@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.doc(security='Bearer Auth')
    @api.expect(review_model)
    @api.marshal_with(review_output_model, code=201)
    @api.response(400, 'Invalid input data.')
    def post(self):
        """Register a new review"""
        user_id = get_jwt_identity()
        review_data = api.payload
        review_data['user_id'] = user_id
        place = facade.get_place(review_data['place_id'])

        if not place:
            api.abort(400, 'Place not found.')
        if not user_id:
            api.abort(400, 'User not found.')

        if place.owner_id == user_id:
            api.abort(400, 'You cannot review your own place.')
        
        existing_review = facade.get_review_by_user_and_place(user_id, review_data['place_id'])
        if existing_review:
            api.abort(400, 'You have already reviewed this place.')
        review_data['user_id'] = user_id
        try:
            new_review = facade.create_review(review_data)
            return new_review, 201
        except Exception as e:
            api.abort(400, str(e))

    @api.marshal_with(review_output_model, as_list=True)
    @api.response(200, 'List of reviews retrieved successfully.')
    def get(self):
        """Retrieve a list of all reviews"""
        return facade.get_all_reviews(), 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @jwt_required()
    @api.doc(security='Bearer Auth')
    @api.marshal_with(review_output_model)
    @api.response(200, 'Review details retrieved successfully.')
    @api.response(404, 'Review not found.')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, 'Review not found.')
        return review, 200

    @jwt_required()
    @api.doc(security='Bearer Auth')
    @api.expect(review_model)
    @api.response(200, 'Review updated successfully.')
    @api.response(404, 'Review not found.')
    @api.response(400, 'Invalid input data.')
    @api.response(403, 'Unauthorized action.')
    def put(self, review_id):
        """Update a review's information"""
        current = get_jwt_identity()
        is_admin = current.get('is_admin', False) if isinstance(current, dict) else False
        user_id = current.get('id') if isinstance(current, dict) else current
       
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, 'Review not found.')

        if not is_admin and review.get("user_id") != user_id:
            api.abort(403, 'Unauthorized action.')

        review_data = api.payload

        text = review_data.get('text', '').strip()
        if not text:
            api.abort(400, 'Review text cannot be empty.')
        review_data['text'] = text

        rating = review_data.get('rating')
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            api.abort(400, 'Rating must be an integer between 1 and 5.')


        try:
            facade.update_review(review_id, review_data)
            updated_review = facade.get_review(review_id)
            return updated_review, 200
        except Exception as e:
            api.abort(400, str(e))

    @jwt_required()
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Review deleted successfully.')
    @api.response(404, 'Review not found.')
    @api.response(403, 'Unauthorized action.')
    def delete(self, review_id):
        """Delete a review"""
        current = get_jwt_identity()
        is_admin = current.get('is_admin', False) if isinstance(current, dict) else False
        user_id = current.get('id') if isinstance(current, dict) else current
       
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, 'Review not found.')

        if not is_admin and review.get("user_id") != user_id:
            api.abort(403, 'Unauthorized action.')


        try:
            facade.delete_review(review_id)
            return {'message': 'Review deleted successfully.'}, 200
        except Exception as e:
            api.abort(400, str(e))
