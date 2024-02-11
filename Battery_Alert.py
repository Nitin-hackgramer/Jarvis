from Jarvis import speak
from psutil import sensors_battery

check = None
check_Fully_Charged = None
charge_status = False
speak("running Battery Alert")
while True:
    battery_percentage = sensors_battery().percent

    if sensors_battery().power_plugged and charge_status != True:
        speak("charging")
        charge_status = True

    elif not sensors_battery().power_plugged:
        charge_status = False

    elif battery_percentage == 100 and check_Fully_Charged != 100:
        speak("sir, Laptop is Fully Charged Now, you can remove the charger")
        check_Fully_Charged = 100

    elif battery_percentage < 100:
        check_Fully_Charged

    elif battery_percentage < 20 and check != 20 and check != 10:
        speak("sir, Battery is below 20%")
        check = 20

    elif battery_percentage <= 10 and check != 10:
        speak("sir, Battery is below 10%, I think You Should put it on charge now")
        check = 10

    elif battery_percentage > 20:
        check = None
