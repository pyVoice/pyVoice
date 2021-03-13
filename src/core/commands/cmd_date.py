from datetime import datetime
import locale

from src import settings
from src.core.modules import tts, replying

# says the date


def ex(cmd):
    try:
        locale.setlocale(locale.LC_TIME, settings.LANGUAGE.replace("-", "_"))
    except locale.Error:
        try:
            locale.setlocale(
                locale.LC_TIME, settings.LANGUAGE.replace("-", "_") + ".utf-8"
            )
        except locale.Error:
            print("Your locale was not found, using default one")

    date = datetime.now()

    day = date.strftime("%d").lstrip("0")
    month = date.strftime("%B")
    year = date.strftime("%Y")

    tts.speak(replying.get_reply("date").format(day, month, year))
