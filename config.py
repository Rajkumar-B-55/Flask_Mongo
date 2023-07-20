import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

    # database credentials
    DB_NAME = os.environ.get('DB_NAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_COLLECTION = os.environ.get('DB_COLLECTION')
