"""
**Logging module**

Logs messages to the configured logging output.
"""

import logging

from src import settings

logger = logging.getLogger(settings.LOGGER_NAME)
logger.setLevel(settings.LOGGER_LEVEL)


def error(text: str) -> None:
    """
    Log a error message

    Args:
        text (str): The message to log
    """

    if logger.level <= logging.ERROR:
        print("\n- {}".format(text))
    logger.info(text)


def debug(text: str) -> None:
    """
    Log a debug message (helpful for development)

    Args:
        text (str): The message to log
    """

    if logger.level <= logging.DEBUG:
        print("\n- {}".format(text))
    logger.debug(text)


def info(text: str) -> None:
    """
    Log a informative message

    Args:
        text (str): The message to log
    """

    if logger.level <= logging.INFO:
        print("\n- {}".format(text))
    logger.info(text)
