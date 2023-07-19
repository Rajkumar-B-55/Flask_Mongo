from flask import jsonify, request, make_response, Blueprint

from app.models.models import User
from app.services.jwt_svc import UserAuth, token_required
from app.services.logging_svc import LoggingService
from app.services.user_svc import UserService

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


@blueprint.route('/register', methods=['POST'])
def register_user():
    try:
        request_json = request.json
        response, status_code = UserService.register_user(request_json)
        response_json = response.get_json()
        return jsonify(response=response_json, status=status_code)
    except Exception as e:
        LoggingService.app.error(
            F"Exception on Create new employee")
        return make_response(jsonify({'error': str(e)}), 400)


@blueprint.route('/login', methods=['POST'])
def user_login():
    request_json = request.json
    user = User.by_username(request_json['email'])
    if user:
        auth_token, expiration_time = UserAuth.login(
            incoming_password=request_json['password'],
            hashed_password=user.password,
            user_id=user._id,
            user_email=user.email
        )
        LoggingService.app.info(
            F" User_id: {user._id}, logged in")
        return jsonify({'token': auth_token, 'expires_in': expiration_time}), 200
    else:
        LoggingService.app.error(
            "user not found")
        return make_response(
            jsonify({'error': 'user not found '}), 404)


@blueprint.route('/update', methods=['PUT'])
@token_required
def update_user(current_user):
    try:
        request_json = request.json
        response, status_code = UserService.update_user(request_json, current_user)
        response_json = response.get_json()
        return jsonify(response=response_json, status=status_code)
    except Exception as e:
        LoggingService.app.error(
            F"Exception on Update User")
        return make_response(jsonify({'error': str(e)}), 400)


@blueprint.route('/get', methods=['GET'])
@token_required
def get_user(current_user):
    try:
        response, status_code = UserService.get_user(current_user)
        response_json = response.get_json()
        LoggingService.app.info(
            F" Get employee by user_email:{current_user.email}")
        return jsonify(response=response_json, status=status_code)

    except Exception as e:
        LoggingService.app.error(
            F"Exception on Get user")
        return make_response(jsonify({'error': str(e)}), 400)


@blueprint.route('/delete', methods=['DELETE'])
@token_required
def delete_user(current_user):
    try:
        response, status_code = UserService.delete_user(current_user)
        response_json = response.get_json()
        LoggingService.app.info(
            F" Delete User by user_email:{current_user.email}")
        return jsonify(response=response_json, status=status_code)
    except Exception as e:
        LoggingService.app.error(
            F"Exception on Delete user")
        return make_response(jsonify({'error': str(e)}), 400)
