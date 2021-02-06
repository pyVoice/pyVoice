from src.core.modules import tts


def ex(cmd):
    tts.speak(cmd["input"].replace(cmd["text"] + " ", ""))
