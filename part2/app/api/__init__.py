from flask import Flask
from flask_restx import Api

def create_app():
    """
    Create and configure the flask application
    with Flask-RestX API.
    """
    app = Flask(__name__)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
    )

    # Placeholder for API namespaces (endpoints will be added later)
    # Additional namespaces for places, reviews, and amenities will be added later
    
    return app
