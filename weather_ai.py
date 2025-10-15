import win32com.client
import requests
import json
import speech_recognition as sr
import pyaudio

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.speak("Hello, I am Weather AI!! your weather assistant. Give me your location to get the current weather update.")

def city_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🙉Listening...")
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            speaker.speak("Sorry, I did not understand that. Please try again.")
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speaker.speak("Could not request results; check your network connection.")
            print("Could not request results; check your network connection.")
            return None
        
speaker.speak("Would you like to speak your city or type it?")
choice = input("🤔Do you want to speak your city? (yes/no): ").strip().lower()
if choice not in ["yes", "no"]:
        print("Invalid choice. Please enter 'yes' or 'no'.")


if choice == "yes":
    city = None
    while city is None:
        city = city_input()
else:
    city = input("Please type your city: ").strip()

API_KEY = "982a1df29ac690f6e6a9d21f48ec2322"  
weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(weather_api)

if response.status_code == 200:
    weather_data = response.json()

    weather = weather_data["weather"][0]["description"]
    main = weather_data["main"]
    wind = weather_data["wind"]
    clouds = weather_data["clouds"]
    sys = weather_data["sys"]
    visibility = weather_data.get("visibility", "N/A")
    name = weather_data["name"]

    report = (
        f"Current weather in {name}: {weather}. \n"
        f"Temperature is {main['temp']}°C, feels like {main['feels_like']}°C. \n"
        f"Minimum temperature is {main['temp_min']}°C and maximum temperature is {main['temp_max']}°C.\n "
        f"Humidity is at {main['humidity']}%. \n"
        f"Wind speed is {wind['speed']} m/s. \n"
        f"Cloudiness is {clouds['all']}%. \n"
        f"Visibility is {visibility} meters.\n"
    )

    speaker.speak("Fetching weather details...")
    speaker.speak(f"Here is the weather report: {report}")
    print(f"Reports📃\n{report}\n")
    speaker.speak("Thanks!!\nHave a great day!")
    print(f"🙏Thanks!!\n🤗Have a great day!")

else:
    error_msg = "Sorry, I couldn't fetch the weather details. Please check the city name."
    speaker.speak(error_msg)
    print(error_msg)
