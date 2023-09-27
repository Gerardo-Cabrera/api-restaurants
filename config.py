import os

class Config:
    # Set this to True to enable automatic reloading during development
    FLASK_ENV = 'production'

    # Database configuration
    if FLASK_ENV == 'production':
        SQLALCHEMY_DATABASE_URI = 'postgresql://cbtfaqzrlbqqft:dac8088db5a7059b6a35613e708ca3e1e665948d0499532778497ea9d77d4e44@ec2-44-206-204-65.compute-1.amazonaws.com:5432/d6r7nfbh2slmmu'
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/database'
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CSV file path
    CSV_FILE_PATH = 'https://recruiting-datasets.s3.us-east-2.amazonaws.com/restaurantes.csv'

    # Development environment setting
    DEBUG = True

    # Add other configuration options here
