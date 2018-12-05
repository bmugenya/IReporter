class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}


"""This module contains the various app configurations"""
import os


class Config():
    """ Base config (other configs inherit from this base)"""
    DEBUG = False
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Development Config"""
    DEBUG = True
    DATABASE_CONNECTION_URL = os.getenv('DATABASE_CONNECTION_URL')


class TestingConfig(Config):
    """Testing Config"""
    TESTING = True
    DEBUG = True
    DATABASE_CONNECTION_URL = os.getenv('DATABASE_CONNECTION_URL')


class ProductionConfig(Config):
    """Production Config"""
    DEBUG = False
    TESTIN = False


app_configuration = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

secret_key = Config.SECRET
