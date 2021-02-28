import sys
import os
from pathlib import Path
import json
from platform import platform

from src import settings

file_path = "./data/settings.json" if getattr(sys, "frozen", False) and hasattr(sys,
                                                                                "_MEIPASS") is True else "src/data/settings.json"


def write_os_json() -> None:
    os = platform()

    with open(file_path, "r") as file:
        orig_file = json.load(file)

    orig_file["operating_system"] = os

    with open(file_path, "w") as new_file:
        json.dump(orig_file, new_file, indent=2)


def load_settings() -> dict:
    with open(file_path, "r") as settings_file:
        return json.load(settings_file)


def create_log_dir() -> None:
    """
    Creates the logs directory, to store the log files made by the application.

    Steps:
        1. Extracts the file name from the path using the `os.path.dirname` function
        2. Creates the path using `Path` from `pathlib`
    """
    path_name = os.path.dirname(os.path.abspath(settings.FILE_LOGGER_PATH))
    Path(path_name).mkdir(parents=True, exist_ok=True)


def run_startup_tasks() -> None:
    write_os_json()
