from pymongo.mongo_client import MongoClient
import urllib


class NoSQlConfig:
    client = None
    db = None
    collection = None

    @classmethod
    def initialize_database_connection(cls, app):
        from config import Config

        MONGO_URI = f"mongodb+srv://{Config.DB_USERNAME}:{urllib.parse.quote(Config.DB_PASSWORD)}@{Config.DB_HOST}/{Config.DB_NAME}?retryWrites=true&w=majority"
        cls.client = MongoClient(MONGO_URI)
        cls.db = cls.client[Config.DB_NAME]
        cls.collection = cls.db[Config.DB_COLLECTION]

        return cls.client, cls.db, cls.collection
