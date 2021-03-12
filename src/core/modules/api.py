import requests
from src import settings
from src.core.modules import log, utils


def register_device() -> None:
    api_url = settings.API_URL
    os = utils.get_operating_system()
    id = utils.get_device_id()
    version = settings.VERSION
    location = utils.get_location()

    # device data
    req_data = {
        "device_id": id,
        "operating_system": os,
        "version": version,
        "location": location,
    }
    req_headers = {"Authorization": "Api-Key " + settings.API_KEY}

    try:
        req = requests.post(api_url, data=req_data, headers=req_headers)
    except Exception:
        log.error("An error ocurred with the API request")

    # debug only
    print(req_data)
    print(req.text)

    if req.status_code == 201:
        log.info("Registered installation in database!")
        utils.switch_registered_field()
    else:
        log.error("An error ocurred while registering the device")
