"""
**Logging module**

Logs messages to the configured logging output.
"""

import logging

from src import settings
from src.core.modules.startup import create_log_dir

create_log_dir()

logger = logging.getLogger(settings.LOGGER_NAME)

file_logger = logging.FileHandler(settings.FILE_LOGGER_PATH)
file_logger.setFormatter(
    logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
    )
)

logger.addHandler(file_logger)
logger.setLevel(settings.LOGGER_LEVEL)


def error(text: str) -> None:
    """
    Logs a error message

    Args:
        text (str): The message to log
    """

    if logger.level <= logging.ERROR:
        print("\n- {}".format(text))
    logger.info(text)


def debug(text: str) -> None:
    """
    Logs a debug message (helpful for development)

    Args:
        text (str): The message to log
    """

    if logger.level <= logging.DEBUG:
        print("\n- {}".format(text))
    logger.debug(text)


def info(text: str) -> None:
    """
    Logs a informative message

    Args:
        text (str): The message to log
    """

    if logger.level <= logging.INFO:
        print("\n- {}".format(text))
    logger.info(text)
