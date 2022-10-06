


from tkinter import *
from datetime import datetime
from time import strftime

w = Tk()
w.geometry("350x180")
w.title("Digital Clock")

f1=Frame(w, width=820,height=200, bg="black")
#f1.place(x=0,y=0)
f1.pack(anchor = "center")

def time():
    a=strftime("%x \n %A \n %H:%M:%S %p")
    l1.config(text=a)
    l1.after(1000,time)
    
l1=Label(f1, font=("ds-digital",40),bg="black",foreground="cyan")
l1.place(x=34,y=10)
time()

w.mainloop()






