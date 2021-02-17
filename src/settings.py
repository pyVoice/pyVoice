"""
Settings
"""

import logging
import sys
from platform import platform

from src import __version__

KEYWORD = "hey"

LANGUAGE = "en-US"
LANGUAGE_SHORT = LANGUAGE[:2]

LOCATION = "lisbon"
WEATHER_API_KEY = ""
SENTRY_DSN = "https://08c7d197057a44e1b07ab43c1d0691ce@o520978.ingest.sentry.io/5632072"

STT_ENGINE = "google"
TTS_ENGINE = ""
TTS_SUBTITLE = True
TTS_AUTODETECT = True

OPERATING_SYSTEM = platform()
VERSION = __version__
ENV = "dev"

# check if running in bundle mode or dev/normal mode
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    ACTIVATION_SOUND_PATH = "./data/sound/activation.mp3"
    PHRASES_FILE_PATH = "./data/json/phrases.json"
    REPLIES_FILE_PATH = "./data/json/replies.json"
else:
    ACTIVATION_SOUND_PATH = "src/data/sound/activation.mp3"
    PHRASES_FILE_PATH = "src/data/json/phrases.json"
    REPLIES_FILE_PATH = "src/data/json/replies.json"

MAX_NEWS_TICKS = 3

SR_ENERGY_THRESHOLD = 200

LOGGER_NAME = "pyvoice"
LOGGER_LEVEL = logging.DEBUG
