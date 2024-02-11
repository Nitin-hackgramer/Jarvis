from Bard import Bard_AI
from pyttsx3 import init
import webbrowser as w
import datetime
import time as t
from os import system
from wikipedia import summary
from pyautogui import hotkey, typewrite, sleep
from psutil import sensors_battery
import speech_recognition as sr


def speak(texts):
    """Function Convert Text to Speech"""
    engine = init("sapi5")
    engine.setProperty("voice", (engine.getProperty("voices"))[0].id)
    engine.setProperty("rate", 175)
    engine.say(texts)
    engine.runAndWait()


def greet():
    """Function Greet When Program runs"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Ram Ram Sir")
    elif 12 <= hour < 18:
        speak("Ram Ram sir")
    elif 18 <= hour <= 24:
        speak("Ram Ram Sir")
    speak("I am Jarvis. Please tell me how may I help you")


def takeCommand():
    """This is a Backup function for STT(Speech to Text)"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == "__main__":
    greet()
    while True:
        query = ""  # query = takeCommand()
        file = open("output_file.txt", "r")
        data = file.read()
        file.close()
        file_history = open("history_chat.txt", "r")
        data_history = file_history.read()
        file_history.close()

        if str(data) == str(data_history):
            t.sleep(0.5)
            pass

        else:
            query = data.lower()
            file_history = open("history_chat.txt", "w")
            file_history.write(data)
            file_history.close()

        # Casual talkies
        if "hello" in query:
            speak("Hello sir")

        elif "kya hal hai" in query or "kya hal chaal" in query:
            speak("I am Great sir, how about you?")

        elif "how are you" in query or "how r u" in query:
            speak("I am good sir, How are you")

        elif "who are you" in query or "hu r u" in query:
            speak("I am Jarvis sir, An Assistant to Help You")

        elif "who created you" in query or "tumhen kisne banaya" in query:
            speak("I am Jarvis, a Desktop Assistent Creatod by Nitin Sharma")

        elif "date" in query:
            speak(f"it's {datetime.date.today()}")

        elif "time" in query or "kitne baj gaye" in query or "kya baj gaye" in query:
            print(datetime.datetime.now().strftime("%I:%M:%S %p"))
            speak(f"its {datetime.datetime.now().strftime('%I:%M %p')}")

        elif "tum ladki ho ya ladka" in query or "tum ladka ho ya ladki" in query:
            speak("Sir, I'm a Boy, Please show some respect")

        elif query == "shutdown laptop":
            system("shutdown /s /t 1")

        elif "bhago yahan se" in query or "sleep" in query:
            speak("okay sir, happy to help you")
            break

        elif "kaun sa de" in query:
            print(datetime.datetime.now().strftime("%A"))
            speak("sir, I think you should take some almond for a good memory, by the way Today is" + datetime.datetime.now().strftime("%A"),)

        elif "battery" in query or "Kitna charge" in query or "charge Kitna" in query:
            speak(f"it's {sensors_battery().percent}%")

        elif "bird" in query:
            Query = query.replace("bird", "").replace(" ", "")
            speak("one minute sir")
            data = Bard_AI(query=Query)
            print("Bard:- ", data)
            speak(data)

        # For You Tube
        elif "band" in query or "shuru" in query or "stop" in query or "chalu" in query:
            hotkey("k")

        elif "mute" in query:
            hotkey("m")

        elif "full screen" in query or "exit full screen" in query:
            hotkey("f")

        # Websites
        elif "wikipedia" in query:
            speak(
                f'searching{query.replace(" wikipedia", "").query.replace("search", "").replace("jarvis", "").replace("on ", "")} on wikipedia'
            )
            info = summary(query.replace(" wikipedia", ""), sentences=2)
            print(info)
            speak(f"According to Wikipedia {info}")

        elif "search" in query:
            speak(
                f'searching {query.replace("search", "").replace("jarvis", "").replace("on google ", "").replace(" ", "")} on google'
            )
            w.open(
                "https://www.google.com/search?q="
                + query.replace(" search", "")
                .replace("jarvis", "")
                .replace("on google", "")
                .replace(" ", "")
            )

        elif "play " in query:
            speak(
                f'playing {query.replace(" on youtube", "").replace("play ", "").replace("in", "").replace("jarvis","")} on youtube'
            )
            w.open(
                "https://www.youtube.com/results?search_query="
                + query.replace(" on youtube", "")
                .replace("play", "")
                .replace("in", "")
                .replace("jarvis", "")
            )

        # Applications
        elif "open" in query or "chalao" in query or "chalaio" in query:
            query = (
                query.replace("jarvis", "")
                .replace("open", "")
                .replace("chalu", "")
                .replace("karo", "")
                .replace("chalao", "")
                .replace("kario", "")
                .replace("chaalu", "")
                .replace("kholo", "")
                .replace("chalaio", "")
                .replace(" ", "")
            )
            if "youtube" in query:
                speak("launching youtube")
                system("start www.youtube.com")

            elif "monkeytype" in query:
                speak("Launching Monkey type")
                system("start https://www.monkeytype.com")

            elif ".com" in query or ".co.in" in query or ".org" in query:
                system(f"start https://{query}")

            else:
                hotkey("win")
                typewrite(query)
                sleep(0.5)
                hotkey("enter")

        elif "new tab" in query:
            hotkey("ctrl", "t")

        elif "reload" in query:
            hotkey("ctrl", "r")

        elif "minimise" in query:
            hotkey("alt", "space")
            sleep(0.5)
            hotkey("N")

        elif "close" in query:
            hotkey("ctrl", "w")
