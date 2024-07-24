import os
import speech_recognition as sr
import pyaudio
import gtts
from gtts import gTTS
while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        print("text=",r.recognize_google(audio))
        
    except sr.unknownValueError:
        print("nopr")
    except sr.RequestError as e:
        print("nop")
