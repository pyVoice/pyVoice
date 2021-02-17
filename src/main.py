import sys
import traceback

from src import settings
from src.core.modules import log, tts, stt, matching, replying

# TODO: make quit work


class Assistant:
    def __init__(self):
        self.setup()
        self.stop = False

    def setup(self) -> None:
        log.debug("Setup...")

        # Initialize engines
        stt.setup()
        tts.setup()

    def clean(self) -> None:
        log.debug("Cleaning...")

    def greet(self) -> None:
        log.debug("Greeting...")

        # print banner and basic usage
        print(settings.BANNER)
        print(replying.get_reply("greet", system=True).format(settings.KEYWORD))
        print(replying.get_reply("greet", system=True, stage=1).format(settings.KEYWORD))
        print(replying.get_reply("greet", system=True, stage=2).format(settings.KEYWORD))

        tts.speak(replying.get_reply("greet", system=True, stage=3))

    def quit(self) -> None:
        log.debug("Quitting...")

        self.stop = True
        self.clean()

        log.info("Bye!")
        sys.exit()

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
                    matching.execute_match(cmd)
            except KeyboardInterrupt:
                log.info("Detected keyboard interruption...")
                self.quit()
                break
            except:
                log.error("Unexpected error...")
                traceback.print_exc()
                break
