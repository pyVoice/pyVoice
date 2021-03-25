import requests

from src import settings
from src.core.modules import log, tts, replying


def ex(cmd):
    country_name = settings.COUNTRY.lower()

    api_url = "https://api.covid19api.com/total/country/{0}/status/confirmed".format(
        country_name
    )

    try:
        res = requests.get(api_url).json()[-1]
        total_cases = res["Cases"]

        tts.speak(
            replying.get_reply("covid").format(country_name.capitalize(), total_cases)
        )
    except requests.ConnectionError:
        log.error("An error ocurred while loading the data, try again later...")
    except:
        log.error("An error ocurred, try again later...")
