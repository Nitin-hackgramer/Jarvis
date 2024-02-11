from Jarvis import speak
from datetime import datetime

if __name__ == "__main__":
    speak("running Study Schedule")
    while True:
        if (
            int(datetime.now().hour) == 10
            and int(datetime.now().minute) == 0
            and int(datetime.now().second) == 0
        ):
            speak("Sir It's Time to learn Some Maths")
        elif (
            int(datetime.now().hour) == 12
            and int(datetime.now().minute) == 0
            and int(datetime.now().second) == 0
        ):
            speak(
                "Sir, Enough Learning for today, it's been 2 hours"
            )
        elif (
            int(datetime.now().hour) == 15
            and int(datetime.now().minute) == 0
            and int(datetime.now().second) == 0
        ):
            speak("Sir It's Time to learn Some Physics")
        elif (
            int(datetime.now().hour) == 17
            and int(datetime.now().minute) == 0
            and int(datetime.now().second) == 0
        ):
            speak(
                "Sir, Enough Learning for today, it's been 2 hours"
            )
        elif (
            int(datetime.now().hour) == 19
            and int(datetime.now().minute) == 0
            and int(datetime.now().second) == 0
        ):
            speak("Sir It's Time to learn Some Chemistry")
        elif (
            int(datetime.now().hour) == 20
            and int(datetime.now().minute) == 0
            and int(datetime.now().second) == 0
        ):
            speak(
                f"Sir, its {datetime.now().strftime('%I:%M %p')} I think It's time to bought some milk"
            )
        elif (
            int(datetime.now().hour) == 20
            and int(datetime.now().minute) == 30
            and int(datetime.now().second) == 0
        ):
            speak("Sir It's Time to learn Chemistry Again")
        elif (
            int(datetime.now().hour) == 21
            and int(datetime.now().minute) == 30
            and int(datetime.now().second) == 0
        ):
            speak(
                "Sir, Enough Learning for today, it's been an hours"
            )
