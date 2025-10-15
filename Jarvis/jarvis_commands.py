import os
import webbrowser
import datetime
import pyjokes  
import wikipedia

def command(query):
    if "open youtube " in query:
        webbrowser.open("youtube.com")
    elif "shudown" in query:
        os.system("shutdown /s /t 0")
    elif "wikipedia" in query:
        speak("searching...")
        query = query.replce("wikipedia", "")
        result = wikipedia.summary(query,sentence = 10)
        speak(result)
    elif "jokes" in query:
        speak(pyjokes.get_jokes())
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    else:
        speak("i can't do that yet")

while True:
    query = listen()
    if listen == "":
        speak()