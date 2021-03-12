from src.core.modules import tts, replying, api, utils


def ex(cmd) -> None:
    try:
        if utils.check_if_registered() is False:
            api.register_device()
            tts.speak(replying.get_reply("register_install", stage=0))
        else:
            tts.speak(replying.get_reply("register_install", stage=2))
    except Exception:
        tts.speak(replying.get_reply("register_install", stage=1))
