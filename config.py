import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SECRET_KEY = 'teste123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/manutenção_luz_local"


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'teste123'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/manutenção_luz_local"
