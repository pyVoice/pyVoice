import webbrowser

from commands.date_time import date
from utils.audio import speak, record_audio


def respond(voice_data):
    if 'data' in voice_data:
        date()
    if 'sair' in voice_data:
        exit()
    if 'pesquisar' in voice_data:
        search = record_audio('O que devo procurar?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Aqui está o que encontrei para: ' + search)


# time.sleep(1)
speak('Em que posso ajudar?')

# operating cycle (infinite loop)
while 1:
    voice_data = record_audio()
    respond(voice_data)
