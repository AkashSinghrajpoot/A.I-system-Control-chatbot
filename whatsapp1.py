import pywhatkit
import pyttsx3
import datetime
import speech_recognition
from datetime import timedelta
from time import sleep
import webbrowser
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

# Dictionary to store recipient names and phone numbers

recipient_contacts = {
    "akhilramola": "+919**881",
    "akhil ramola": "+919****571",
    "Akhil": "+91***171", 

    "house": "+91***907881",
    "akhil chandra mola": "+917*****81", 
    "anand": "+91++++++001",
    "boss": "+91@@@@830",
    
}    


def speak(audio):
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
        except Exception as e:
            print("Say that again")
            return "None"
        return query

def sendMassage():
    speak("Whom do you want to message, sir?")
    recipient_name = takeCommand().lower()
    if recipient_name == "none":
        recipient_name = input("Enter the name: ")

    # Check if the recipient name is in the dictionary
    if recipient_name in recipient_contacts:
        recipient_phone_number = recipient_contacts[recipient_name]
    else:
        speak(f"Sorry, I don't have the contact information for {recipient_name}.")
        return

    speak("What message would you like to send?")
    message_content = takeCommand()
    if message_content.lower() == "none":
        return

    speak("At what time do you want to send the message? Please provide the time in 24-hour format. You can also say 'current time'.")
    time_input = takeCommand().lower()

    if "current time" in time_input:
        current_time = datetime.datetime.now() + timedelta(minutes=1)
        pywhatkit.sendwhatmsg(recipient_phone_number, message_content, current_time.hour, current_time.minute + 1, wait_time=30)
        
        pyautogui.press("enter")
        
        
            
  # Add 1 minute to the current time
    else:
        hour = int(input("Enter hour: "))
        minute = int(input("Enter minute: "))
        current_time = datetime.datetime.now()
        scheduled_time = datetime.datetime(current_time.year, current_time.month, current_time.day, hour, minute)

        if scheduled_time <= current_time:
            speak("Invalid time. Please provide a future time.")
            return

    time_difference = current_time - datetime.datetime.now()
    minutes_until_send = divmod(time_difference.total_seconds(), 60)[0]

    speak(f"The message will be sent to {recipient_name} in {minutes_until_send} minutes.")

    # Wait for the specified time before sending the message
    sleep(minutes_until_send * 60)

    # Send the message using pywhatkit
    pywhatkit.sendwhatmsg(recipient_phone_number, message_content, scheduled_time.hour, scheduled_time.minute + 1)
    sleep(40)
    pyautogui.press("enter")
    

# Uncomment the line below to test the function
# sendMassage()
