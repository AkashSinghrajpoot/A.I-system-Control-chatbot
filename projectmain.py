import pyttsx3
import speech_recognition
from GreetMe import greetMe  # Assuming GreetMe is a module in the same directory
import requests
from bs4 import BeautifulSoup
import datetime
import os
import openai
from whatsapp1 import sendMassage
import pyautogui
from webecam import webcamera
from Repley import ReplyIt

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    print(f"Speaking: {audio}")  # Debugging if speak is called
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
        try:
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except Exception:
            print("Say that again")
            return "None"
        return query

def Mic():
    query = takeCommand()
    data = query
    print(f"You: {data}.")
    return data



if __name__ == "__main__":
    
    greetMe()
    
    while True:
        query = takeCommand().lower()
        
        # General commands
        if "go to sleep" in query:
            speak("Ok sir, you can call me any time")
            break
        elif "hello" in query:
            speak("Hello sir. How are you?")
        elif "how are you" in query:
            speak("Same as you, my dear")
        elif "who is your boss" in query:
            speak("Mister Akash Singh is my boss.")
        elif "tell me about your boss" in query or "tell me about akash singh" in query:
            speak("Akash Singh Rajpoot, a software engineer and data scientist, is a successful businessman passionate about innovation, collaboration, and making a positive impact.")
        elif "tell me about yourself" in query or "give me your introduction" in query:
            speak("I am ichchha, working for my boss as his A.I. personal assistant.")
        elif "what is your name" in query:
            speak("My name is ichchha.")
        elif "introduction with our team" in query:
            speak("Our team name is A3, group number four, consisting of three members: Akash Singh Rajpoot, Amit Kumar, and Akhil Chand Ramola.")
        elif "who are you" in query:
            speak("I am ichchha.")
        elif "who is our mentor" in query:
            speak("Doctor Amit Kumar Pandey.")
        elif "i love you" in query:
            speak("Love you more, my sweet heart.")
        
        # Open applications
        elif "open" in query:
            Query = query.replace("open", "").replace("ichchha", "").replace("start", "").replace("search", "").strip()
            pyautogui.press("super")
            pyautogui.sleep(3)
            pyautogui.typewrite(Query)
            
            pyautogui.press("enter")

        # Web searches and specific commands
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        elif "temperature" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")
        
        # WhatsApp and Screenshot
        elif "whatsapp" in query:
            sendMassage()
        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("photo")
        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.sleep(2)
            pyautogui.press("enter")
            speak("Smile!")

            pyautogui.press("enter")
        
        # Fallback to OpenAI Response
        
                
            
            
