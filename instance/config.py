import os


class Config():
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_CONNECTION_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE_CONNECTION_URL = os.getenv('DATABASE_URL')


class ProductionConfig(Config):
    DEBUG = False
    TESTIN = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
