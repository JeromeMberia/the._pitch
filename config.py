import os

class Config:
    '''
    parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jerome:1234@localhost/pitch'

class ProdConfig(Config):
    '''
    production configurations child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jerome:1234@localhost/pitch'

    DEBUG = True

config_options = {
 'development': DevConfig,
 'production': ProdConfig
}