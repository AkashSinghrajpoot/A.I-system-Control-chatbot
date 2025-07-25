import speech_recognition
import pyttsx3
import pywhatkit 
import wikipedia
import webbrowser



def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening......")
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

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query :
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google","")
        query = query.replace("googlesearch","")
        query = query.replace("wikipedia","")
        query = query.replace("search","")
        query = query.replace("iccha","")
        query = query.replace("ichcha","")
        query = query.replace("about","")
        query = query.replace("google search","")
        speak("this is what i found for only you on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            speak(result)

        except:
            speak("no speakble output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("this is what i found")
        query = query.replace("jarvis","")
        query = query.replace("youtube","")

        query = query.replace("youtubesearch","")
        query = query.replace("utube","")
        query = query.replace("search","")
        query = query.replace("iccha","")
        query = query.replace("ichcha","")
        query = query.replace("about","")
        query = query.replace("youtube search","")
        web = "https://www.youtube.com/results?search_query="+ query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done ,sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching from wikipedia......")
        query = query.replace("wikipedia")
        query = query.replace("wikipediasearch","")
        query = query.replace("jarivs","")
        query = query.replace("search","")
        query = query.replace("iccha","")
        query = query.replace("ichcha","")
        query = query.replace("about","")
        query = query.replace("information","")
        results = wikipedia.summary(query,sentences = 2)
        speak("according to wikipedia")
        print(results)
        speak(results)        

        