from gtts import gTTS
from playsound import playsound
audio='speech.mp3'
language='en'
sp=gTTS(text = 'my name is lalit and im a good programmer',
        lang=language,slow=False)
sp.save(audio)
playsound(audio)