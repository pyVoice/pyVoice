import json

from src import settings
from src.core.modules import tts, replying

# TODO: replace by sys module in paths


def ex(cmd):
    with open("data/files/json/notes.json", "r+", encoding="utf-8") as notes_file:
        notes_file_data = json.load(notes_file)

    new_note = cmd["input"].replace(cmd["text"] + " ", "")

    notes_file_data["notes"].append(new_note)

    with open("data/files/json/notes.json", "w", encoding="utf-8") as notes_file:
        json.dump(notes_file_data, notes_file, indent=2, ensure_ascii=False)

    tts.speak(replying.get_reply("note_add").format(new_note))
