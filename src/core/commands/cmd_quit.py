from src.core.modules import tts, replying


def ex(cmd):
    tts.speak(replying.get_reply("quit"))
