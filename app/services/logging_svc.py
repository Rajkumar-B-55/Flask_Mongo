import logging


class LoggingService:
    logger = None
    app = None

    @classmethod
    def initialize(cls, app):
        logging.basicConfig(filename='record.log', level=logging.DEBUG,
                            format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.DEBUG)
        cls.app = app.logger
        cls.app.info("app loger initialized")
        cls.logger.info("loger initialized")