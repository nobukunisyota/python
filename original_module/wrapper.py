from logging import getLogger, StreamHandler, Formatter, DEBUG


def log_decoletor(func):
    def get_logger():
        logger = getLogger(__name__)
        logger.propagate = False
        handler = StreamHandler()
        handler.setFormatter(
            Formatter('[%(levelname)s][%(asctime)s][func:%(message)s]'))
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)
        return logger

    def wrapper(*args, **kwargs):
        logger = get_logger()
        logger.debug(f'{func.__name__}')
        func(*args, **kwargs)
        logger.debug(f'{func.__name__}')
    return wrapper
