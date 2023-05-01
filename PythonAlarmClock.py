from datetime import datetime, time
import os
import threading
import time
from playsound import playsound
from tkinter import *

class AlarmClock:
    """
    A GUI-based alarm clock that allows the user to set an alarm and select a sound file to play when the alarm goes off.

    Attributes:
    root (Tk): The Tkinter root window.
    alarm_time (datetime.time): The time at which the alarm should go off.
    sound_file (str): The path to the sound file that should play when the alarm goes off.
    snooze_time (int): The number of seconds to snooze the alarm.
    alarm_thread (threading.Thread): The thread that checks the current time and plays the sound file when the alarm time is reached.
    play_sound_thread (threading.Thread): The thread that plays the sound file.
    """
    def __init__(self, root):
        """
        Initializes the AlarmClock.

        Args:
        root (Tk): The Tkinter root window.
        """
        self.root = root
        self.alarm_time = None
        self.sound_file = None
        self.snooze_time = None
        self.alarm_thread = None
        self.play_sound_thread = None
        self.create_gui()

    def create_gui(self):
        """
        Creates the GUI for the AlarmClock.
        """
        self.root.title("Alarm Clock")

        # Create hour label and entry
        hour_label = Label(self.root, text="Hour:")
        hour_label.grid(row=0, column=0)
        self.hour_entry = Entry(self.root, width=5)
        self.hour_entry.grid(row=0, column=1)

        # Create minute label and entry
        minute_label = Label(self.root, text="Minute:")
        minute_label.grid(row=0, column=2)
        self.minute_entry = Entry(self.root, width=5)
        self.minute_entry.grid(row=0, column=3)

        # Create set alarm button
        self.set_alarm_button = Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.grid(row=1, column=0, columnspan=2)

        # Create select sound button
        self.select_sound_button = Button(self.root, text="Select Sound", command=self.select_sound)
        self.select_sound_button.grid(row=1, column=2, columnspan=2)

        # Create snooze label and entry
        snooze_label = Label(self.root, text="Snooze (s):")
        snooze_label.grid(row=2, column=0)
        self.snooze_entry = Entry(self.root, width=5)
        self.snooze_entry.grid(row=2, column=1)

        # Create snooze button
        snooze_button = Button(self.root, text="Snooze", command=self.snooze)
        snooze_button.grid(row=2, column=2)

        # Create stop alarm button
        self.stop_alarm_button = Button(self.root, text="Stop Alarm", command=self.stop_alarm, state=DISABLED)
        self.stop_alarm_button.grid(row=2, column=3)

    def set_alarm(self):
        """
        Sets the alarm time.
        """
        # Get hour and minute from user input
        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())

        # Set alarm time
        self.alarm_time = time(hour=hour, minute=minute)

        # Disable input fields and buttons
        self.hour_entry.config(state=DISABLED)
        self.minute_entry.config(state=DISABLED)
        self.select_sound_button.config(state=DISABLED)
        self.set_alarm_button.config(state=DISABLED)
        self.snooze_entry.config(state=NORMAL)

        # Start alarm thread
        self.alarm_thread = threading.Thread(target=self.check_time)
        self.alarm_thread.start()

    def select_sound(self):
        """
        Opens a file dialog to allow the user to select a sound file.
        """
        self.sound_file = filedialog.askopenfilename()

    def snooze(self):
        """
        Snoozes the alarm for the specified number of seconds.
        """
        self.stop_alarm()

        # Get snooze time from user input
        self.snooze_time = int(self.snooze_entry.get())

        # Start alarm thread again with updated alarm time
        self.alarm_time = datetime.now().time() + timedelta(seconds=self.snooze_time)
        self.alarm_thread = threading.Thread(target=self.check_time)
        self.alarm_thread.start()

    def stop_alarm(self):
        """
        Stops the alarm and resets the GUI.
        """
        # Stop alarm thread
        if self.alarm_thread:
            self.alarm_thread.cancel()
            self.alarm_thread = None

        # Stop sound thread
        if self.play_sound_thread:
            self.play_sound_thread.cancel()
            self.play_sound_thread = None

        # Reset GUI
        self.hour_entry.delete(0, END)
        self.hour_entry.config(state=NORMAL)
        self.minute_entry.delete(0, END)
        self.minute_entry.config(state=NORMAL)
        self.set_alarm_button.config(state=NORMAL)
        self.select_sound_button.config(state=NORMAL)
        self.snooze_entry.delete(0, END)
        self.snooze_entry.config(state=DISABLED)
        self.stop_alarm_button.config(state=DISABLED)

    def check_time(self):
        """
        Checks the current time and plays the sound file if the alarm time is reached.
        """
        while True:
            # Get current time
            now = datetime.now().time()

            # If current time matches alarm time, play sound file
            if now >= self.alarm_time:
                self.play_sound()
                break

            # Sleep for 1 second before checking again
            time.sleep(1)

    def play_sound(self):
        """
        Plays the sound file.
        """
        # Disable snooze and stop alarm buttons
        self.snooze_entry.config(state=DISABLED)
        self.stop_alarm_button.config(state=NORMAL)

        # Play sound file in a separate thread
        self.play_sound_thread = threading.Thread(target=playsound, args=(self.sound_file,))
        self.play_sound_thread.start()

if __name__ == "__main__":
    root = Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()

