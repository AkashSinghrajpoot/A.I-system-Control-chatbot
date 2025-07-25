import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
dictapp ={"commandprompt": "cmd","paint":"paint" ,"word" :"winword" ,"excel":"excel" ,"chrome":"chrome","vscode" :"code","powerpoint" : "powerpoint"}

def openappweb(query):
    speak("launching sir")
    if ".com" in query or  ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("ichcha","")
        query = query.replace("launch","")
        query = query.replace("","")
        webbrowser.open(f"https://wwww.{query}")
    else:
        keys =list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab" in query or "to tab" in query or "two tab" in query :
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed sir")
    elif "3 tab" in query or "three tab" in query :
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed sir")       
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed sir")      
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed sir") 
    elif "6 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed sir")

    else:
        keys = list(dictapp.keys())
        for app in query:
            if app in query:
                os.system(f"taskkill /f / in {dictapp[app]}.exe")                        