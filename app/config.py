# -*- coding:UTF-8 -*-


class Config(object):
    DB_USER = 'root'  # type: str
    DB_PASSWORD = ''  # type: str
    DB_HOST = 'localhost'  # type: str
    DB_DB = 'flask-pyjwt-auth'  # type: str
    DEBUG = False  # type: bool
    PORT = 8080  # type: int
    HOST = "0.0.0.0"  # type: str
    SECRET_KEY = "my blog"  # type: str
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # type: # bool
    SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
    ENV = 'Production'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    PORT = 5002  # type: int
    HOST = "127.0.0.1"  # type: str
    DEBUG = True
    ENV = 'Development'


class TestingConfig(Config):
    TESTING = True


