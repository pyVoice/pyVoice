import traceback

from printy import printy
from pyfiglet import Figlet
from sentry_sdk import capture_exception

from src import settings
from src.core.modules import log, matching, replying, sentry, startup, stt, tts


class Assistant:
    def __init__(self):
        self.fig = Figlet(font="larry3d")
        self.setup()
        self.stop = False

    def setup(self) -> None:
        log.debug("Setup...")

        # Initialize engines
        startup.run_startup_tasks()
        sentry.setup()
        stt.setup()
        tts.setup()

    def greet(self) -> None:
        log.debug("Greeting...")

        printy(self.fig.renderText("pyVoice"), "nB")
        print(replying.get_reply("greet", system=True).format(settings.KEYWORD))
        print(
            replying.get_reply("greet", system=True, stage=1).format(settings.KEYWORD)
        )
        print(
            replying.get_reply("greet", system=True, stage=2).format(settings.KEYWORD)
        )

        tts.speak(replying.get_reply("greet", system=True, stage=3))

    def quit(self) -> None:
        log.debug("Quitting...")

        self.stop = True

        log.info("Bye!")
        exit(code=0)

    def run(self):
        self.greet()

        while True:
            if self.stop:
                break

            try:
                if stt.listen_for_keyword():
                    log.debug("Back in main loop...")

                    audio = stt.listen()
                    audio_input = stt.recognize(audio)

                    if not audio_input:
                        log.info("Couldn't resolve audio...")
                        continue
                    else:
                        log.info("Catched input: '{0}'".format(audio_input))

                    cmd = matching.get_match(audio_input)

                    if cmd["name"] == "quit":
                        self.quit()

                    matching.execute_match(cmd)
            except KeyboardInterrupt:
                log.info("Detected keyboard interruption...")
                self.quit()
                break
            except:
                log.error("Unexpected error...")
                traceback.print_exc()

                # sends the traceback to Sentry
                capture_exception(traceback.print_exc())
                break
