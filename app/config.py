import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    #ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    #ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'Password123'
    UPLOAD_FOLDER = 'uploads/'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://project1:firstproject@localhost/project1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    #MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    #MAIL_PORT = os.environ.get('MAIL_PORT') or '25'
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False