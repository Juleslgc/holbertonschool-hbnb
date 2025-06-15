from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, title='HBnB API', description='API for HBnB project')
    api.add_namespace(users_ns, path='/api/v1/users')
    return app
