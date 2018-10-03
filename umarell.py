import logging
import os
import time
from functools import wraps

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler = logging.FileHandler(os.path.join(os.getcwd(), 'performance.log'))
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)


def umarell(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = (end - start) * 1000
        logging.debug("{}: {} ms".format(func.__name__, round(elapsed, 3)))
        return result

    return wrapper
