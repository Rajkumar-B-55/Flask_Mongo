import logging
import sys


class LoggingService:
    logger = None
    app = None

    @classmethod
    def initialize(cls, app):
        logging.basicConfig(stream=sys.stdout,filename='record.log', level=logging.DEBUG,
                            format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.DEBUG)
        cls.app = app.logger
        cls.app.info("app loger initialized")
        cls.logger.info("loger initialized")
