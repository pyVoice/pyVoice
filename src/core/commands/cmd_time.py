from datetime import datetime

from src.core.modules import tts, replying


def ex(cmd):
    date = datetime.now()

    hour = date.strftime("%H")
    minute = date.strftime("%M")

    tts.speak(replying.get_reply("time").format(hour, minute))
