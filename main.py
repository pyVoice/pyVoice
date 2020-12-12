from respond import Respond
from utils.audio import speak, record_audio

voice_data = ""

respond = Respond(voice_data=voice_data)

# time.sleep(1)

speak('Em que posso ajudar?')

# operating cycle (infinite loop)
while 1:
    voice_data = record_audio()
    print(f'[+] User input: {voice_data}')
    respond.respond()
