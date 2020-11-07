from gtts import gTTS

count = 1
text = 'Your sentence requiring text to speech'
file_path = 'text.mp3'
tts = gTTS(text=text, lang='en', slow=False)
while True:
    try:
        tts.save(file_path)
        break
    except:
        print('got the issue ' + str(count))
        count += 1
