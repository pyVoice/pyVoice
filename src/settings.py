"""
Settings
"""

import logging

KEYWORD = "otto"

LANGUAGE = "en-US"
LANGUAGE_SHORT = LANGUAGE[:2]

LOCATION = "lisbon"
WEATHER_API_KEY = ""

STT_ENGINE = "google"
TTS_ENGINE = ""
TTS_SUBTITLE = True
TTS_AUTODETECT = True

OPERATING_SYSTEM = ""

ACTIVATION_SOUND_PATH = "src/data/files/sound/activation.mp3"
PHRASES_FILE_PATH = "src/data/files/json/phrases.json"
REPLIES_FILE_PATH = "src/data/files/json/replies.json"

MAX_NEWS_TICKS = 3

SR_ENERGY_THRESHOLD = 200

LOGGER_NAME = "otto"
LOGGER_LEVEL = logging.DEBUG
