import pyttsx3
import speech_recognition as robo_voice
import pyaudio


engine = pyttsx3.init()
engine.setProperty("rate",150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    r = robo_voice.Recognizer()
    with robo_voice.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language = "en-in")
        print(f"user said: {query}\n")
    except:
        speak("sorry, i didn't get that.")
        return
    return query.lower()

speak("hello i am sexa. how can i help you?")
query = listen()
speak(f"you said {query}")