from datetime import datetime

from app.models import NoSQlConfig


class Base:
    def __init__(self):
        self.created_on = datetime.utcnow()
        self.updated_on = datetime.utcnow()

    def save(self):
        # Get the MongoDB collection
        collection = NoSQlConfig.collection
        data = self.to_dict()
        # Insert the document into the collection
        result = collection.insert_one(data)
        self._id = result.inserted_id

    def update(self):
        # Get the MongoDB collection
        collection = NoSQlConfig.collection
        data = self.to_dict()
        # Update the document in the collection using its _id
        collection.update_one({"_id": self._id}, {"$set": data})

    def delete(self):
        # Get the MongoDB collection
        collection = NoSQlConfig.collection
        # Delete the document using its _id
        collection.delete_one({"_id": self._id})

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k not in ["_id"]}


class User(Base):
    def __init__(self, first_name, last_name, is_active, email, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.email = email
        self.password = password
        self._id = None

    @classmethod
    def from_document(cls, data):
        user = cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            is_active=data.get("is_active"),
            email=data.get("email"),
            password=data.get("password")
        )
        user.created_on = data.get("created_on")
        user.updated_on = data.get("updated_on")
        user._id = data.get("_id")
        return user

    @classmethod
    def by_id(cls, user_id):
        collection = NoSQlConfig.collection
        user_data = collection.find_one({"_id": user_id})
        if user_data:
            return cls.from_document(user_data)
        return None

    @classmethod
    def by_username(cls, username):
        collection = NoSQlConfig.collection
        user_data = collection.find_one({"email": username})
        if user_data:
            return cls.from_document(user_data)
        return None
