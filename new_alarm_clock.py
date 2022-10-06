from tkinter import *
from datetime import datetime
import time
import winsound

def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        msg = "Current Time: " + str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("harry_potter.WAV", winsound.SND_FILENAME)
            break

def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)



window = Tk()
window.title("Alarm Clock")
window.geometry("400x210")
window.resizable(width = False, height = False)

time_format = Label(window, text= "          Remember to set time in 24 hour format!").place(x = 20, y = 120)
addTime = Label(window,text = "Hour    Min    Sec", font = (15)).place(x = 210)
setYourAlarm = Label(window,text = " Set Time for Alarm: ",font = (23)).place(x = 10, y = 40)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(window, textvariable = hour, width = 4, font=(20)).place(x = 210, y = 40)
minTime = Entry(window, textvariable = min, width = 4, font=(20)).place(x = 270, y = 40)
secTime = Entry(window, textvariable = sec, width = 4, font=(20)).place(x = 330, y = 40)

submit = Button(window, text = "Set Your Alarm", bg="powder blue", width = 15, command = get_alarm_time, font=(20)).place(x = 100, y = 80)
stop = Button(window, text="stop", bg = "powder blue", width=10, command = quit).place(x = 20, y = 170)
stop = Button(window, text="snooze", bg = "powder blue", width=10).place(x = 300, y = 170) 
 
window.mainloop()
