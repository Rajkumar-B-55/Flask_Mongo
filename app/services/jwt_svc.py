import datetime
from functools import wraps

import jwt
from flask import request, make_response, jsonify

from app.models import NoSQlConfig
from app.models.models import User
from app.services.logging_svc import LoggingService
from config import Config
from lib.utils import validate_password


class UserAuth:

    @classmethod
    def login(cls, incoming_password, hashed_password, user_id, user_email):
        if validate_password(incoming_password, hashed_password):
            user_id = str(user_id)
            expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
            payload = {
                'user_id': user_id,
                'user_email': user_email.__str__(),
                'exp': expiration_time
            }
            token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm="HS256")
            return token, expiration_time
        else:
            raise ValueError("Incorrect credentials")

    @classmethod
    def current_user_mongo(cls):
        try:
            token = request.headers.get('x-access-tokens')
            if not token:
                return None
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
            user_id = data.get('user_id')
            collection = NoSQlConfig.collection
            current_user = collection.find_one({"_id": user_id})
            return current_user
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None


def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            LoggingService.app.error("Valid auth token is Missing!")
        try:
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
            current_user = User.by_username(data['user_email'])
        except Exception as e:
            LoggingService.app.error("Invalid token")
            return make_response(jsonify(
                {
                    "Message": "Token is invalid"
                }
            ))
        return fn(current_user, *args, **kwargs)

    return wrapper
