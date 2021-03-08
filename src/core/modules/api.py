import requests

from src import settings
from src.core.modules import log


def get_location() -> str:
    req = requests.get("https://ipinfo.io")
    data = req.json()
    return "{0}, {1}".format(data["city"], data["country"])


def register_device() -> None:
    api_url = settings.API_URL
    os = settings.OPERATING_SYSTEM
    id = settings.DEVICE_ID

    # device data
    req_data = {
        "device_id": id,
        "operating_system": os,
        "version": settings.VERSION,
        "location": get_location(),
    }
    req_headers = {"Authorization": "Api-Key " + settings.API_KEY}

    req = requests.post(api_url, data=req_data, headers=req_headers)

    # debug only
    print(req_data)
    print(req.text)

    if req.status_code == 201:
        log.info("Registered installation in database!")
    else:
        log.error("An error ocurred while registering the device.")
