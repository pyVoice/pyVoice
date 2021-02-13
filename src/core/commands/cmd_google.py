import requests
from bs4 import BeautifulSoup

from src import settings
from src.core.modules import tts

"""
Google Search
"""


def ex(cmd):
    keywords = input.replace(settings.KEYWORD + " ", "").lower().replace(" ", "+")
    url = "https://www.google.com/search?q={0}&hl={1}".format(keywords, settings.LANGUAGE_SHORT)

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")

    try:
        text_tag = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
        output = text_tag.getText()
    except:
        text_tag = soup.find("div", {"class": "xpc"}).find("div", {"class": "BNeawe s3v9rd AP7Wnd"})
        output = text_tag.getText()

    tts.speak(output)
