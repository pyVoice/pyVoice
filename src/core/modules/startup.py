import json
import os
import sys
from pathlib import Path
from platform import platform
from uuid import uuid4

from src import settings

file_path = (
    "./data/settings.json"
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") is True
    else "src/data/settings.json"
)


def create_log_dir() -> None:
    """
    Creates the logs directory, to store the log files made by the application.

    Steps:
        1. Extracts the file name from the path using the `os.path.dirname` function
        2. Creates the path using `Path` from `pathlib`
    """
    path_name = os.path.dirname(os.path.abspath(settings.FILE_LOGGER_PATH))
    Path(path_name).mkdir(parents=True, exist_ok=True)


def check_first_run() -> bool:
    with open(file_path, "r") as file:
        settings_file = json.load(file)

    if settings_file["first_run"] is True:
        return True
    else:
        return False


def switch_settings_field() -> None:
    with open(file_path, "r") as file:
        orig_file = json.load(file)

    orig_file["first_run"] = False

    with open(file_path, "w") as new_file:
        json.dump(orig_file, new_file, indent=2)


def set_device_id() -> None:
    id = str(uuid4())

    with open(file_path, "r") as file:
        orig_file = json.load(file)

    orig_file["device_id"] = id

    with open(file_path, "w") as new_file:
        json.dump(orig_file, new_file, indent=2)


def set_operating_system() -> None:
    os = platform()

    with open(file_path, "r") as file:
        orig_file = json.load(file)

    orig_file["operating_system"] = os

    with open(file_path, "w") as new_file:
        json.dump(orig_file, new_file, indent=2)


def load_settings() -> dict:
    with open(file_path, "r") as settings_file:
        return json.load(settings_file)


def run_startup_tasks() -> None:
    create_log_dir()
    if check_first_run() is True:
        set_device_id()
        set_operating_system()
        # register_device()
        # switch_settings_field()
