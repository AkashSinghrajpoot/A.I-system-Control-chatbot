# GreetMe.py

import pyttsx3
import datetime 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good morning, sir")
    elif 12 <= hour <= 18:
        speak("Good afternoon, sir")
    else:
        speak("Good evening, sir")
    speak("Please tell me how can I help you?")

# Test the greetMe function

