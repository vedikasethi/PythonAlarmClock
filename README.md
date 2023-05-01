# PythonAlarmClock
##Alarm Clock with GUI using Python and Tkinter

###Steps to run the project

1. Clone or download the code from your GitHub repository to your local machine.
2. Ensure that you have Python 3.x installed on your machine. You can download the latest version of Python from the official website at https://www.python.org/downloads/.
3. Open a command prompt or terminal window and navigate to the project directory.
4. Install the `playsound` module and any other dependencies using the following command: `pip install -r requirements.txt`
5. Run the Python script using the following command: `python PythonAlarmClock.py`
6. The alarm clock GUI window will open. Set the alarm time, select a sound file, and specify the snooze time as required.
7. Once the alarm time is reached, the selected sound file will start playing. You can snooze the alarm by specifying the snooze time.

###Abstract:

This project aims to develop an alarm clock with a Graphical User Interface (GUI) using the Python programming language and the Tkinter library. The alarm clock allows the user to set the alarm time, select a sound or music file to play when the alarm goes off, and snooze the alarm for a specified amount of time. The project utilizes the datetime and playsound libraries to play the selected sound or music file when the alarm time is reached. The alarm clock is designed to run in the background while the user works on other tasks and have the ability to play different sounds or music files for each alarm.

###Introduction:

The alarm clock has become a crucial part of our daily routine, helping us to wake up on time and start our day. The traditional alarm clock has now been replaced with modern technology, which allows us to set alarms on our mobile phones, laptops, and other devices. However, it is always beneficial to have a dedicated alarm clock with an intuitive and user-friendly interface.

In this project, we have developed an alarm clock with a GUI using the Python programming language and the Tkinter library. The GUI allows the user to set the alarm time, select a sound or music file to play when the alarm goes off, and snooze the alarm for a specified amount of time. The project utilizes the datetime and playsound libraries to play the selected sound or music file when the alarm time is reached. The alarm clock is designed to run in the background while the user works on other tasks and has the ability to play different sounds or music files for each alarm.

###Methodology:

The alarm clock is developed using the object-oriented programming paradigm in Python. The Tkinter library is used to create the GUI for the alarm clock, which consists of four input fields for hour, minute, sound file selection, and snooze time. The user can set the alarm time by entering the desired hour and minute values, select a sound or music file using the file selection dialog box, and specify the snooze time in seconds.

The alarm clock works by continuously checking the current time against the set alarm time. Once the alarm time is reached, the selected sound or music file is played in a separate thread using the playsound library. The user can snooze the alarm by specifying the snooze time, which will start the alarm again after the specified time has elapsed.

###Results:

The developed alarm clock with a GUI is user-friendly and intuitive, allowing the user to easily set the alarm time, select a sound or music file, and snooze the alarm. The project is designed to run in the background while the user works on other tasks and has the ability to play different sounds or music files for each alarm.

###Conclusion:

The developed alarm clock with a GUI using Python and Tkinter is a useful application for anyone who needs an intuitive and user-friendly alarm clock. The project demonstrates the use of object-oriented programming, the Tkinter library for GUI development, and the playsound library for playing sound or music files. The project can be further extended by adding more features, such as multiple alarms, recurring alarms, and custom alarm sounds.
