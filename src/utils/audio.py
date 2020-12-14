import os
import random

import playsound
import speech_recognition as sr
from gtts import gTTS

from src.config import settings

r = sr.Recognizer()


def record_audio(ask=False):
    """
    Gets audio from the user's microphone

    :param ask:
    :type ask:
    :return:
    :rtype:
    """
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language=settings.LANGUAGE_GOOGLE)
        except sr.UnknownValueError:
            speak('Não consegui entender o que disse.')
        except sr.RequestError:
            speak('O meu serviço está offline.')
        return voice_data


def speak(audio_string):
    """
    Outputs audio from a text string

    :param audio_string:
    :type audio_string:
    :return:
    :rtype:
    """
    tts = gTTS(text=audio_string, lang=settings.LANGUAGE)
    random_int = random.randint(1, 100000)
    audio_file = 'audio-' + str(random_int) + '.mp3'
    tts.save(audio_file)

    playsound.playsound(audio_file)

    if settings.MODE == 'dev':
        print(audio_string)

    os.remove(audio_file)
