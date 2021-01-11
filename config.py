import os
from decouple import config


class Config(object):
    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='Rejusa_S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'postgres://sjoreeikecxojy:a54b64f534606aa3da9ecc009b70632391feb97c99764c55313a247777aee528@ec2-23-20-129-146.compute-1.amazonaws.com:5432/d9818pj5i1shd'
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
