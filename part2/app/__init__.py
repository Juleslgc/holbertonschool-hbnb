from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as user_namespace
from app.api.v1.amenities import api as amenities_namespace
from app.api.v1.places import api as places_namespace
from app.api.v1.reviews import api as reviews_namespace

def create_app():
    """
    Create and config the flask application.
    """
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    api.add_namespace(user_namespace, path='/api/v1/users')
    api.add_namespace(amenities_namespace, path='/api/v1/amenities')
    api.add_namespace(places_namespace, path='/api/v1/places')
    api.add_namespace(reviews_namespace, path='/api/v1/reviews')

    return app