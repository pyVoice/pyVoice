"""
**Text to Speech (TTS) engine**

Converts text into audio.
Works in Windows (using the SAPI engine) and other platforms, using `gTTS`.
"""

import platform
from tempfile import NamedTemporaryFile as named_temp_file

from playsound import playsound

from src import settings
from src.core.modules import log

engine = None


def setup() -> None:
    """
    Initialize the TTS engine

    Steps:
        1. Checks the platform (operating system)
        2. Sets the engine to one supported (SAPI or gTTS)
    """

    global engine

    # detect OS
    if platform.system() == "Windows" and settings.TTS_AUTODETECT:
        try:
            import win32com.client as win32com

            engine = win32com.Dispatch("SAPI.SpVoice")
            log.debug("Using SAPI")
        except ModuleNotFoundError:
            log.error("Couldn't find module named 'win32com.client'")
            log.error("Check installation or install via 'pip install pypiwin32'")
    else:
        try:
            from gtts import gTTS

            engine = gTTS
            log.debug("Using gTTS")
        except ModuleNotFoundError:
            log.error("Couldn't find module named 'gTTS'")
            log.error("Check installation or install via 'pip install gTTS'")

        log.info("(!) Using slow TTS engine on your OS")


def play_mp3(file: str) -> None:
    """
    Plays a MP3 file. Used when engine is set to gTTS.

    Args:
        file (str): the file to play
    """

    if file.endswith(".mp3"):
        playsound(file, True)
    else:
        log.error("The file provided is not a MP3 file.")


def speak(text: str) -> None:
    """
    Outputs a text phrase to audio.

    Steps:
        1. If Windows, play using the SAPI engine. Else, play using gTTS and the `play_mp3` function.

    Args:
        text (str): the text phrase to say
    """

    if settings.TTS_SUBTITLE:
        log.info(text)

    if platform.system() == "Windows" and settings.TTS_AUTODETECT:
        engine.Speak(text)
    else:
        with named_temp_file() as f:
            output = engine(text=text, lang=settings.LANGUAGE_SHORT)
            output.save(f.name + ".mp3")
            play_mp3(f.name + ".mp3")
