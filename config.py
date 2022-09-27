import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'teste123'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
    RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/manutenção_luz_local"
    CACHE_TYPE = "simple"


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    ASSETS_DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/manutenção_luz_local"

    CACHE_TYPE = "null"

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'


class TestConfig(Config):
    TESTING = True

    # DEBUG_TB_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/manutenção_luz_local_teste"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CACHE_TYPE = 'null'
    # CACHE_NO_NULL_WARNING = True
    # WTF_CSRF_ENABLED = False
    #
    # MAIL_SERVER = 'localhost'
    # MAIL_PORT = 25
    # MAIL_USERNAME = 'username'
    # MAIL_PASSWORD = 'password'


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
