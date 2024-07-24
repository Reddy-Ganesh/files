import speech_recognition as sr
import gtts
import os
import pyaudio
while True:
    r=sr.Recognizer()#it is used recognizer the user input
    with sr.Microphone() as source:
        audio =r.listen(source)
    try:
        print("your voice to text",r.recognize_google(audio))

    except sr.unknownValueErro:
        print("cannot understand")
    
    except sr.RequestError as e:
        print("cannot understand")        
