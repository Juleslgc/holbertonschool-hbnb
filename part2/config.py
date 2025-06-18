import os

class Config:
    """
    This is a configuration class for application.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    """
    This is a configuration class for environment.
    Inherits from Config and debug mode
    """
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}