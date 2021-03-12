import json
import os
from pathlib import Path

from src import settings


def create_log_dir() -> None:
    """
    Creates the logs directory, to store the log files made by the application.

    Steps:
        1. Extracts the file name from the path using the `os.path.dirname` function
        2. Creates the path using `Path` from `pathlib`
    """
    path_name = os.path.dirname(os.path.abspath(settings.FILE_LOGGER_PATH))
    Path(path_name).mkdir(parents=True, exist_ok=True)


def load_settings() -> dict:
    with open(settings.settings_file_path, "r") as settings_file:
        return json.load(settings_file)


def run_startup_tasks() -> None:
    create_log_dir()
