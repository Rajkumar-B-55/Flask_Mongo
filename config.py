import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

    # database credentials
    DB_NAME = os.environ['DB_NAME']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_USERNAME = os.environ['DB_USERNAME']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_COLLECTION = os.environ['DB_COLLECTION']
