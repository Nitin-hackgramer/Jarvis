import time
from pygame import mixer
from Jarvis import speak

f = open("Programmer Health.txt", "a")
mixer.init()


def Exercise_Reminder():
    Time = time.asctime(time.localtime())
    time.sleep(5400)
    while True:
        speak("Sir, time for some workout, it's about 1 and half hour")
        if (
            input("Enter 'exdone' to Stop Reminder ") == "exdone"
            or "exercise done" in query
        ):
            mixer.music.stop()
            f.write(f"Done Exercise at:-{Time}\n")
        else:
            print("Wrong Input")


def Eye_Rest_Reminder():
    Time = time.asctime(time.localtime())
    time.sleep(3600)
    while True:
        speak("Sir, Give some rest to your eyes")
        if input("Enter 'eydone' to Stop Reminder ") == "eydone" or "done" in query:
            mixer.music.stop()
            f.write(f"Eyes got some rest at:-{Time}\n")
        else:
            print("Wrong Input")


def Water_Reminder():
    Time = time.asctime(time.localtime())
    time.sleep(7200)
    while True:
        speak("Sir, time to drink some water")
        if input("Enter 'drank' to Stop Reminder ") == "drank" or "drink" in query:
            mixer.music.stop()
            f.write(f"Drank Water at:-{Time}\n")
        else:
            print("Wrong Input")


Water_Reminder()
Eye_Rest_Reminder()
Exercise_Reminder()
f.close()
