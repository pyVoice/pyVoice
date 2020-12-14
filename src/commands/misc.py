import subprocess
from datetime import datetime


class MiscCommands:
    def __init__(self):
        self.command_list = ['note']
        self.note_keywords = ['nota', 'tirar uma nota', 'fazer uma nota']

    @staticmethod
    def note(text):
        date = datetime.now()
        file_name = str(date).replace(':', '-') + '-note.txt'
        with open(file_name, 'w') as f:
            f.write(text)
        subprocess.Popen(['notepad.exe', file_name])

    def get_note_keywords(self):
        return self.note_keywords
