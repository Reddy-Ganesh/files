import os
from gtts import gTTS
myText=input()
myobj =gTTS(text=myText, lang="en",slow=True)
myobj.save("texttospeech.mp3")
os.system("mpg321 texttospeech.mp3")
