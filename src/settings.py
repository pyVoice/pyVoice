"""
Settings
"""

import logging

KEYWORD = "hey"

LANGUAGE = "en-US"
LANGUAGE_SHORT = LANGUAGE[:2]

LOCATION = "lisbon"
WEATHER_API_KEY = ""

STT_ENGINE = "google"
TTS_ENGINE = ""
TTS_SUBTITLE = True
TTS_AUTODETECT = True

OPERATING_SYSTEM = ""

# ACTIVATION_SOUND_PATH = "src/data/sound/activation.mp3"
# PHRASES_FILE_PATH = "src/data/json/phrases.json"
# REPLIES_FILE_PATH = "src/data/json/replies.json"

ACTIVATION_SOUND_PATH = "./data/sound/activation.mp3"
PHRASES_FILE_PATH = "./data/json/phrases.json"
REPLIES_FILE_PATH = "./data/json/replies.json"

MAX_NEWS_TICKS = 3

SR_ENERGY_THRESHOLD = 200

LOGGER_NAME = "otto"
LOGGER_LEVEL = logging.DEBUG

# BANNER = """
#                 _    __      _
#     ____  __  _| |  / /___  (_)_______
#    / __ \/ / / / | / / __ \/ / ___/ _ \
#   / /_/ / /_/ /| |/ / /_/ / / /__/  __/
#  / .___/\__, / |___/\____/_/\___/\___/
# /_/    /____/
# """

BANNER = "pyVoic beta"
