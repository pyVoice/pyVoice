"""
Text to Speech engine
"""

import platform
from tempfile import NamedTemporaryFile as named_temp_file

from playsound import playsound

from src import settings
from src.core.modules import log

engine = None


def setup():
    global engine

    # detect OS
    if platform.system() == "Windows" and settings.TTS_AUTODETECT:
        try:
            import win32com.client as win32com
            engine = win32com.Dispatch("SAPI.SpVoice")
        except ModuleNotFoundError:
            log.error("Couldn't find module named 'win32com.client'")
            log.error(
                "Check installation or install via 'pip install pypiwin32'")
    else:
        try:
            from gtts import gTTS
            engine = gTTS
        except ModuleNotFoundError:
            log.error("Couldn't find module named 'gTTS'")
            log.error(
                "Check installation or install via 'pip install gTTS'")

        log.info("(!) Using slow TTS engine on your OS")

# play MP3


def play_mp3(file):
    if file.endswith(".mp3"):
        playsound(file, True)
    else:
        log.error("The file provided is not a MP3 file.")

# speak


def speak(text):
    if settings.TTS_SUBTITLE:
        log.info(text)

    if platform.system() == "Windows" and settings.TTS_AUTODETECT:
        engine.Speak(text)
    else:
        with named_temp_file() as f:
            output = engine(text=text, lang=settings.LANGUAGE_SHORT)
            output.save(f.name + ".mp3")
            play_mp3(f.name + ".mp3")
