# from flask_restplus import Api
# from flask import Blueprint
#
#
# class SwaggerConfig:
#     swagger_route = None
#     login_parser = None
#     auth_token = None
#     new_user = None
#     update_user = None
#     delete_input = None
#
#     @classmethod
#     def initialize(cls, app):
#         blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
#         api = Api(blueprint)
#         app.register_blueprint(blueprint)
#         cls.swagger_route = api.namespace('flask app', description="Swagger")
#         add_user = api.parser()
#         cls.swagger_inputs(api)
#         cls.auth_token_input(api)
#         # cls.new_user_input(api)
#         # cls.update_user_input(api)
#         # cls.delete_user_input(api)
#
#     @classmethod
#     def swagger_inputs(cls, api):
#         cls.login_parser = api.parser()
#         user_form = cls.login_parser.add_argument('username', type=str, location='form', help='Username/Email',
#                                                   required=True)
#         pwd_form = cls.login_parser.add_argument('password', type=str, location='form', help='Password', required=True)
#
#     @classmethod
#     def auth_token_input(cls, api):
#         cls.auth_token = api.parser()
#         auth_token = cls.auth_token.add_argument('x-access-tokens', type=str, location='headers',
#                                                  help='x-access-tokens',
#                                                  required=True)
# swagger_stack.py

from flask_restplus import Api
from flask import Blueprint


class SwaggerConfig:
    swagger_route = None
    login_parser = None
    auth_token = None
    new_user = None
    update_user = None
    delete_input = None

    @classmethod
    def initialize(cls, app):
        blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
        api = Api(blueprint)
        app.register_blueprint(blueprint)
        cls.swagger_route = api.namespace('flask app', description="Swagger")
        cls.swagger_inputs(api)
        cls.auth_token_input(api)
        cls.new_user_input(api)
        cls.update_user_input(api)
        cls.delete_user_input(api)

    @classmethod
    def swagger_inputs(cls, api):
        cls.login_parser = api.parser()
        user_form = cls.login_parser.add_argument('username', type=str, location='form', help='Username/Email',
                                                  required=True)
        pwd_form = cls.login_parser.add_argument('password', type=str, location='form', help='Password', required=True)

    @classmethod
    def auth_token_input(cls, api):
        cls.auth_token = api.parser()
        auth_token = cls.auth_token.add_argument('x-access-tokens', type=str, location='headers',
                                                 help='x-access-tokens',
                                                 required=True)

    @classmethod
    def new_user_input(cls, api):
        cls.new_user = api.model('User', {
            'first_name': api.fields.String(required=True, description='First Name'),
            'last_name': api.fields.String(required=True, description='Last Name'),
            'email': api.fields.String(required=True, description='Email'),
            'password': api.fields.String(required=True, description='Password'),
        })

    @classmethod
    def update_user_input(cls, api):
        cls.update_user = api.model('User', {
            'first_name': api.fields.String(required=True, description='First Name'),
            'last_name': api.fields.String(required=True, description='Last Name'),
            'password': api.fields.String(required=True, description='Password'),
        })

    @classmethod
    def delete_user_input(cls, api):
        cls.delete_input = api.model('User', {
            'password': api.fields.String(required=True, description='Password'),
        })
