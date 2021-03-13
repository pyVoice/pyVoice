import time
import requests
from bs4 import BeautifulSoup


from src import settings
from src.core.modules import tts, replying


def ex(cmd):
    tts.speak(replying.get_reply("news"))

    if settings.LANGUAGE == "pt-PT":
        url = "https://news.google.com/?hl=pt-PT&gl=PT-PT&ceid=PT:pt"
    elif settings.LANGUAGE == "en-US":
        url = "https://news.google.com/?hl=en-US&gl=US&ceid=US:en"

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")

    class_name = "ipQwMb ekueJc RD0gLb"
    tags = soup.find_all("h3", {"class": class_name})

    tts.speak(replying.get_reply("news", stage=1))

    ticks = 0
    for tag in tags:
        ticks += 1
        title = tag.getText()
        tts.speak(title)
        if ticks >= settings.MAX_NEWS_TICKS:
            break
