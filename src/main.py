from time import sleep

from config.settings import WAKE_WORD
from respond import Respond
from utils.audio import record_audio

voice_data = ""

respond = Respond()

sleep(1)

# speak('Em que posso ajudar?')

# operating cycle (infinite loop)
# while 1:
#     voice_data = record_audio()
#     print(f'[+] User input: {voice_data}')
#     respond.respond(voice_data)

# cycle with keywork detection
while True:
    print('[*] Listening')
    voice_data = record_audio()

    if voice_data.count(WAKE_WORD) > 0:
        respond.respond('Estou pronta')
        voice_data = record_audio()
        print(f'[+] User input: {voice_data}')
        respond.respond(voice_data)
