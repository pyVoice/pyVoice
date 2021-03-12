"""
Settings
"""

import logging
import sys

from src import __version__
from src.core.modules.startup import load_settings


settings_file_path = (
    "./data/settings.json"
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") is True
    else "src/data/settings.json"
)

# read from settings JSON file
settings_file_data = load_settings()


KEYWORD = settings_file_data["keyword"]

LANGUAGE = settings_file_data["language"]
LANGUAGE_SHORT = settings_file_data["language"][:2]

LOCATION = settings_file_data["location"]
WEATHER_API_KEY = settings_file_data["weather_api_key"]
SENTRY_DSN = settings_file_data["sentry_dsn"]

STT_ENGINE = settings_file_data["stt_engine"]
TTS_ENGINE = settings_file_data["tts_engine"]
TTS_SUBTITLE = settings_file_data["tts_subtitle"]
TTS_AUTODETECT = settings_file_data["tts_autodetect"]

VERSION = __version__.__version__

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    # Bundled/installed mode
    ACTIVATION_SOUND_PATH = settings_file_data["paths"]["bundled"]["activation_sound"]
    PHRASES_FILE_PATH = settings_file_data["paths"]["bundled"]["phrases_file"]
    REPLIES_FILE_PATH = settings_file_data["paths"]["bundled"]["replies_file"]
    NOTES_FILE_PATH = settings_file_data["paths"]["bundled"]["notes_file"]
else:
    # Dev/normal mode
    ACTIVATION_SOUND_PATH = settings_file_data["paths"]["dev"]["activation_sound"]
    PHRASES_FILE_PATH = settings_file_data["paths"]["dev"]["phrases_file"]
    REPLIES_FILE_PATH = settings_file_data["paths"]["dev"]["replies_file"]
    NOTES_FILE_PATH = settings_file_data["paths"]["dev"]["notes_file"]

MAX_NEWS_TICKS = settings_file_data["max_news_ticks"]

SR_ENERGY_THRESHOLD = settings_file_data["sr_energy_threshold"]

LOGGER_NAME = settings_file_data["logger_name"]
LOGGER_LEVEL = logging.DEBUG
FILE_LOGGER_PATH = settings_file_data["file_logger_path"]

API_KEY = settings_file_data["api_key"]
API_URL = settings_file_data["api_url"]
IS_REGISTERED = settings_file_data["registered"]

ENV = (
    "prod"
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") is True
    else "dev"
)