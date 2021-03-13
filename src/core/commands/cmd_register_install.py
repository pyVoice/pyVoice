from src.core.modules import tts, replying, api, utils


def ex(cmd) -> None:
    if utils.check_if_registered() is False:
        # tries to register the install
        res = api.register_install()

        # check if an error ocurred
        if "detail" in res:
            tts.speak(replying.get_reply("register_install", stage=1))
        else:
            utils.switch_registered_field()
            tts.speak(replying.get_reply("register_install", stage=0))
    else:
        tts.speak(replying.get_reply("register_install", stage=2))
