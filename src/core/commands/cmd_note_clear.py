import json

from src import settings
from src.core.modules import tts, replying


def ex(cmd):
    notes_file_data = {
        "notes": []
    }

    with open(settings.NOTES_FILE_PATH, "w", encoding="utf-8") as notes_file:
        json.dump(notes_file_data, notes_file, indent=2, ensure_ascii=False)

    tts.speak(replying.get_reply("note_clear"))
