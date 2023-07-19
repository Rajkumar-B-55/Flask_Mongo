from flask import jsonify

from app.models.models import User
from lib.utils import encode_password


class UserService:
    @classmethod
    def register_user(cls, req_json):

        """
    Register a new user.

    Expects JSON data in the request body with the following fields:
    - first_name
    - last_name
    - email
    - password

    Returns:
        JSON response with a message indicating successful registration.
    """
        try:
            first_name = req_json['first_name']
            last_name = req_json['last_name']
            email = req_json['email']
            password = req_json['password']

            # Check if the user already exists
            existing_user = User.by_username(email)
            if existing_user:
                return jsonify({'message': 'User with this email already exists'}), 400
            user = User(first_name=first_name, last_name=last_name, is_active=True, email=email,
                        password=encode_password(password))
            user.save()
            return jsonify({'message': 'User registered successfully'}), 201
        except Exception as e:
            raise e

    @classmethod
    def build_user_info(cls, user):
        user_dict = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
        return user_dict

    @classmethod
    def update_user(cls, req_json, user):
        try:
            user = User.by_id(user._id)
            if not user:
                raise ValueError("User not found")

            user.first_name = req_json['first_name']
            user.last_name = req_json['last_name']
            user.password = encode_password(req_json['password'])
            user.update()
            return jsonify({'message': 'User Updated successfully', "info": cls.build_user_info(user)}), 201

        except Exception as e:
            raise e

    @classmethod
    def get_user(cls, user):
        try:
            user = User.by_id(user._id)
            if not user:
                raise ValueError("User not found")
            return jsonify({"info": cls.build_user_info(user)}), 201
        except Exception as e:
            raise e

    @classmethod
    def delete_user(cls, user):
        try:
            user = User.by_id(user._id)
            if not user:
                raise ValueError("User not found")
            user.delete()
            return jsonify(
                {
                    "message": F"User Deleted Successfully"
                }
            ), 202
        except Exception as e:
            raise e
