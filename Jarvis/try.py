import pyttsx3
import speech_recognition as robo_voice
import pyaudio
import os
import webbrowser
import wikipedia
import datetime
import pyjokes

engine = pyttsx3.init()
engine.setProperty("rate", 200)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speech(text):
    engine.say(text)
    engine.runAndWait

def mass():
    r = robo_voice.Recognizer()
    with robo_voice.Microphone() as source:
        print("listing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(f"user: {query}")
    except:
        print("didn't hear that!!")

    def commmand(query):
        if "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "shutdown" in query:
            os.system("shutdown /s /t 0")
        elif "wikipedia" in query:
            speak

