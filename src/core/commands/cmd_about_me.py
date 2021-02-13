from src import settings
from src.core.modules import tts


def ex(cmd):
    tts.speak("I am pyVoice, a voice assistant created by Afonso Santos. You can call me {0}".format(settings.KEYWORD))
