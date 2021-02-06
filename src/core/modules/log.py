"""
Logging module
"""

import logging

from src import settings

logger = logging.getLogger(settings.LOGGER_NAME)
logger.setLevel(settings.LOGGER_LEVEL)


# error
def error(text):
    if logger.level <= logging.ERROR:
        print("\n- {}".format(text))
    logger.info(text)

# debug


def debug(text):
    if logger.level <= logging.DEBUG:
        print("\n- {}".format(text))
    logger.debug(text)

# info


def info(text):
    if logger.level <= logging.INFO:
        print("\n- {}".format(text))
    logger.info(text)
