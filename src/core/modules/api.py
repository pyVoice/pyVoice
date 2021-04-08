import json
import requests
from src import settings
from src.core.modules import log, utils


def register_install() -> json:
    api_url = settings.API_URL

    # system info/telemetry
    os = utils.get_operating_system()
    id = utils.get_device_id()
    version = settings.VERSION
    location = utils.get_location()

    req_data = {
        "device_id": id,
        "operating_system": os,
        "version": version,
        "location": location,
    }

    try:
        req = requests.post(api_url, data=req_data)
    except Exception:
        log.error("An error ocurred with the API request.")

    # debug only
    # print(req_data)
    # print(req.text)

    return req.json()
