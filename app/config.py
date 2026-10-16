import os
from dotenv import load_dotenv

# Load variables from .env into the environment
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))


class Config:
    """Base configuration shared across environments."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-dev-key-change-me')

    # Flask-WTF
    WTF_CSRF_ENABLED = True

    # Flask-Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    # Where contact form submissions are sent
    CONTACT_RECEIVER_EMAIL = os.environ.get('CONTACT_RECEIVER_EMAIL')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'


# Map string names -> config classes (used by the app factory)
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}