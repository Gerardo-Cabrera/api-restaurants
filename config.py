import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://neo:G168652426@localhost:5432/restaurants_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CSV file path
    CSV_FILE_PATH = 'https://recruiting-datasets.s3.us-east-2.amazonaws.com/restaurantes.csv'

    # Development environment setting
    DEBUG = True

    # Set this to True to enable automatic reloading during development
    FLASK_ENV = 'development'

    # Add other configuration options here
