from flask import Flask, Response

from app.models import NoSQlConfig
from app.services.logging_svc import LoggingService
from config import Config


class AppFactory:
    @classmethod
    def create_app(cls):
        try:
            flask_app = Flask(__name__)
            config_settings = Config()
            flask_app.config['JWT_SECRET_KEY'] = config_settings.JWT_SECRET_KEY
            # from app.api.swagger_stack import SwaggerConfig
            # SwaggerConfig.initialize(flask_app)
            LoggingService.initialize(flask_app)
            NoSQlConfig.initialize_database_connection(flask_app)
            from app.api.api import blueprint
            flask_app.register_blueprint(blueprint)
            with flask_app.app_context():
                pass

            @flask_app.route('/health_check')
            def health_check():
                flask_app.logger.debug("main debug")
                flask_app.logger.info("main info")
                flask_app.logger.warning("main warning")
                flask_app.logger.error("main error")
                flask_app.logger.critical("main critical")
                return Response('success', status=200)

            return flask_app
        except Exception as e:
            print(e)
