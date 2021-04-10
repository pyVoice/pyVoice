from platform import platform
from uuid import uuid4
import json

import requests

from src import settings


def get_device_id() -> str:
    return str(uuid4())


def get_operating_system() -> str:
    return platform()


def get_location() -> str:
    req = requests.get("https://ipinfo.io")
    data = req.json()
    return "{0}, {1}".format(data["city"], data["country"])


def check_if_registered() -> bool:
    with open(settings.settings_file_path, "r") as file:
        settings_file = json.load(file)

    if settings_file["registered"] is True:
        return True
    else:
        return False


def switch_registered_field() -> None:
    with open(settings.settings_file_path, "r") as file:
        orig_file = json.load(file)

    orig_file["registered"] = True

    with open(settings.settings_file_path, "w") as new_file:
        json.dump(orig_file, new_file, indent=2)
