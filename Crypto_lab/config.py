import os

class Config:
    # Secret key for CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///crypto_lab.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other configurations (if needed)
