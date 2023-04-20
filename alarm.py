from tkinter import *
import datetime
import time
import pygame

def sound_alarm():
    """Function to play the alarm sound"""
    pygame.mixer.init()
    pygame.mixer.music.load('C:/allPythonProjects/AlarmClock/alarm_sound.mp3')
    pygame.mixer.music.play(3) # Play sound three times


def set_alarm():
    """Function to set the alarm time"""
    alarm_time = entry.get()
    if alarm_time != "":
        alarm_hour = int(alarm_time[0:2])
        alarm_minute = int(alarm_time[3:5])
        alarm_second = int(alarm_time[6:8])
        alarm_time_formatted = datetime.time(alarm_hour, alarm_minute, alarm_second)
        return alarm_time_formatted
    else:
        return None


def check_alarm():
    """Function to check if the alarm time has been reached"""
    alarm_time = set_alarm()
    if alarm_time is not None:
        while True:
            now = datetime.datetime.now().time()
            if now >= alarm_time:
                sound_alarm()
                break
            time.sleep(1)

# Create a tkinter window
window = Tk()
window.title("Alarm Clock")

# Add a label to the window
label = Label(window, text="Enter alarm time (HH:MM:SS):", font=("Arial", 14))
label.pack(pady=10)

# Add an entry widget to the window
entry = Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# Add a button to set the alarm
button = Button(window, text="Set Alarm", font=("Arial", 14), command=check_alarm)
button.pack(pady=10)

# Start the tkinter event loop
window.mainloop()
