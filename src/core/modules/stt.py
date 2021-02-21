"""
**Speech to Text (STT) engine**

Converts the user speech (audio) into text.
"""

import threading
import traceback
import speech_recognition as sr

from src import settings
from src.core.modules import log, tts, replying


def setup() -> None:
    """
    Initializes the STT engine

    Steps:
        1. Creates a new `Recognizer` object
        2. Configures the energy threshold
    """

    global recognizer

    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = settings.SR_ENERGY_THRESHOLD


def listen() -> sr.AudioData:
    """
    Listens for user input (voice) and returns it

    Returns:
        sr.AudioData: The raw input data
    """

    with sr.Microphone() as raw_microphone_input:
        log.debug("Listening to ambient...")
        audio = recognizer.listen(raw_microphone_input)
        return audio


def recognize(audio: sr.AudioData) -> str:
    """
    Transcribes human voice data from a `AudioData` object (from `listen`)

    Args:
        audio (sr.AudioData): The raw audio data from the user

    Returns:
        str: A sentence/phrase with the user intent
    """

    output = None

    log.debug("Recognizing audio...")

    if settings.STT_ENGINE == "google":
        try:
            output = recognizer.recognize_google(audio, language=settings.LANGUAGE)
        except sr.UnknownValueError:
            log.debug("Speech engine could not resolve audio")
        except sr.RequestError:
            log.error("An error ocurred with the Google services, try again")
        except:
            traceback.print_exc()
            log.error("A unknown error ocurred...")
        finally:
            return output


def recognize_keyword() -> None:
    """
    Listens for the keyword, to activate the assistant.

    Steps:
        1. Listens for audio from the microphone
        2. Recognizes the audio using `gTTS`
        3. Checks if the keyword (as in `settings.KEYWORD`) is in the audio data (if True, break loop)
    """

    global keyword_detected
    global new_process

    audio = listen()
    new_process = True
    log.debug("Recognizing keyword...")

    try:
        input = recognizer.recognize_google(audio, language=settings.LANGUAGE)

        if settings.KEYWORD in input.lower():
            log.debug("Keyword detected!")
            # stop listening
            keyword_detected = True
        else:
            log.debug("Keyword not detected in '{0}'".format(input))
    except sr.UnknownValueError:
        log.debug("Speech engine could not resolve audio")
    except sr.RequestError:
        log.error("An error ocurred with the Google services, try again")
    except:
        traceback.print_exc()
        log.error("A unknown error ocurred...")


# listen for keyword, returns True if detected
def listen_for_keyword() -> bool:
    """
    Loops until the keyword is recognized from the user input (from `recognize_keyword`).

    Steps:
        1. Enters the loop (keyword detection)
        2. Creates a new thread (using `recognize_keyword` as target)
        3. If the keywork is detected, break the loop and play the activation sound

    Returns:
        bool: Whether the keyword is recognizes or not. If not, continue the loop.
    """

    global keyword_detected
    global new_process

    log.debug("Keyword loop...")

    keyword_detected = False
    new_process = True

    log.info("Waiting for '{0}'...".format(settings.KEYWORD))

    while True:
        if keyword_detected:
            break

        if new_process:
            new_process = False
            threading.Thread(target=recognize_keyword).start()

    tts.play_mp3(settings.ACTIVATION_SOUND_PATH)
    return True


# listen for binary answer (yes/no), returns True/False
def listen_for_binary() -> bool:
    """
    Checks if a binary/boolean value (Yes/No) is present in the transcribed audio.
    Used in Yes/No questions (e.g. *"Do you want X?"*)

    Steps:
        1. Listens for audio from the microphone
        2. Recognizes the audio using `gTTS`
        3. Checks if a boolean value (Yes, No, True, False) is present in the audio data

    Returns:
        bool: Wheter a boolean value is present in the audio data
    """

    yes_reply = replying.get_reply(["stt", "yn_y"], system=True, module=True)
    no_reply = replying.get_reply(["stt", "yn_n"], system=True, module=True)

    log.info("Waiting for {0} or {1}".format(yes_reply, no_reply))

    while True:
        audio = listen()
        input = recognize(audio)

        if input:
            if yes_reply in input.lower():
                log.debug("'{0}' detected".format(yes_reply))
                return True
            elif no_reply in input.lower():
                log.debug("'{0}' detected".format(no_reply))
                return False
            else:
                log.debug("Not detected binary answer in {0}".format(input))
