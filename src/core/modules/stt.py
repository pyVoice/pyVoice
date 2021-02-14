"""Speech to text"""

import threading
import traceback
import speech_recognition as sr

from src import settings
from src.core.modules import log, tts, replying


def setup():
    global recognizer
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = settings.SR_ENERGY_THRESHOLD

# returns audio from microphone when finished


def listen():
    with sr.Microphone() as raw_microphone_input:
        log.debug("Listening to ambient...")
        audio = recognizer.listen(raw_microphone_input)
        return audio

# returns text output from audio input


def recognize(audio: str):
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

# recognizes the keywork, stops listening of keyword is detected
# callback of listen_for_keyword


def recognize_keyword():
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
def listen_for_keyword():
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
def listen_for_binary():
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
