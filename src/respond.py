import webbrowser

from src.commands.date_time import DateTimeCommands
from src.commands.misc import MiscCommands
from src.utils.audio import speak, record_audio


class Respond:
    def __init__(self):
        self.datetime = DateTimeCommands()
        self.misc = MiscCommands()

    def respond(self, voice_data):
        """
        Checks for the keywork the user sayed and answers
        :return: an action or voice output
        :rtype:
        """
        if any(keyword in voice_data for keyword in self.datetime.get_date_keywords()):
            self.datetime.speak_date()
        if 'sair' in voice_data:
            speak('Adeus!')
            exit()
        if 'pesquisar' in voice_data:
            search = record_audio('O que devo procurar?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Aqui está o que encontrei para: ' + search)
        if any(keyword in voice_data for keyword in self.misc.get_note_keywords()):
            self.misc.note(voice_data)
