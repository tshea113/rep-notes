class Config(object):
    # Base Configuration
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'super_secret'
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Security Config
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'super_salty'
    SECURITY_EMAIL_SENDER = 'youremailhere@gmail.com'

    # Mail Config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'youremailhere@gmail.com'
    MAIL_PASSWORD = 'super_secret'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True