import webbrowser

from commands.date_time import DateTimeCommands
from utils.audio import speak, record_audio


class Respond:
    def __init__(self, voice_data):
        self.datetime = DateTimeCommands()
        self.voice_data = voice_data

    def respond(self):
        """
        Checks for the keywork the user sayed and answers
        :return: an action or voice output
        :rtype:
        """
        if any(keyword in self.voice_data for keyword in self.datetime.get_date_keywords()):
            self.datetime.speak_date()
        if 'sair' in self.voice_data:
            exit()
        if 'pesquisar' in self.voice_data:
            search = record_audio('O que devo procurar?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Aqui está o que encontrei para: ' + search)
