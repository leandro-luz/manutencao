
class Config(object):
    debug = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/manutenção_luz_local"
    #SQLALCHEMY_ECHO = True
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
