import pyttsx3

engine = pyttsx3.init()

# properties
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 95)

print("welcome to robo speaker v1.1 created by Divy S. Shekhwat🤩")
while True:
    start = input("Want to pronounce (y/n): ").lower()
    if start == "y":
        user_voice = input("Type your text: ")
        engine.say(user_voice)
        engine.runAndWait()

    else:
        print("Thanks for trying!!")
        break
