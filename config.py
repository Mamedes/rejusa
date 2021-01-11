import os
from decouple import config


class Config(object):
    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='Rejusa_S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'postgres://epvsjwnimjekma:9ddfa5c2fa6192fabead0da0e252be5523a9edfc0d0b7b3a54e4e184ca527fca@ec2-54-85-80-92.compute-1.amazonaws.com:5432/d8ke0qpti6e9bs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='postgres'),
        config('DB_PASS', default='postgres'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=5432),
        config('DB_NAME', default='rejusa')
    )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
