import json
import requests

from src import settings
from src.core.modules import log, tts, replying


def ex(cmd):
    url = "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&lang={2}&units=metric".format(
        settings.LOCATION, settings.WEATHER_API_KEY, settings.LANGUAGE_SHORT)

    data = requests.get(url)
    content = json.loads(data.text)

    if "message" in content:
        log.error(content["message"])
        tts.speak("An error ocurred: " + content["message"])
    else:
        temp = content["main"]["temp"]
        temp_max = content["main"]["temp_max"]
        description = content["weather"][0]["description"]

        tts.speak(replying.get_reply("weather").format(settings.LOCATION, temp, description, temp_max))
