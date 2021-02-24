import sys
import json
from platform import platform

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


def run_startup_tasks() -> None:
    write_os_json()
