# -*- coding: utf-8 -*-
"""Application configuration."""

import os


class Config(object):
    """Base configuration."""

    DEBUG = False
    TESTING = False
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = 'simple'
    BCRYPT_LOG_ROUNDS = 13
    CSRF_ENABLED = True
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

    MONGODB_DB = os.environ.get('WHERENO_DB', 'whereno')
    MONGODB_HOST = os.environ.get('WHERENO_HOST', 'localhost')
    MONGODB_PORT = os.environ.get('WHERENO_PORT', 27017)
    MONGODB_USERNAME = os.environ.get('WHERENO_USERNAME', 'whereno')
    MONGODB_PASSWORD = os.environ.get('WHERENO_PASSWORD', 'whereno')


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    TESTING = True
    CACHE_TYPE = 'simple'
    BCRYPT_LOG_ROUNDS = 4


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4

