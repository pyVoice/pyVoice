from src.core.modules import tts, replying


def ex(input):
    tts.speak(replying.get_reply("help"))
