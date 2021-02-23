import json
import time

from src import settings
from src.core.modules import tts, replying


def ex(cmd):
    with open(settings.NOTES_FILE_PATH, "r+", encoding="utf-8") as notes_file:
        notes_file_data = json.load(notes_file)

    tts.speak(replying.get_reply("note_read"))

    if len(notes_file_data["notes"]) == 0:
        tts.speak(replying.get_reply("notes_read", stage=1))
    else:
        for note in notes_file_data["notes"]:
            tts.speak(note)
            time.sleep(0.5)
