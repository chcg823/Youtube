# Importing modules
import sys
import time
from tkinter import *

# defining showFunction method
def showTime():
    currentTime = time.strftime("%H:%M:%S")
    clock.config(text=currentTime)
    clock.after(200,showTime)


# GUI
root = Tk()
root.geometry("300x200")

#Labels
clock = Label(root, font="times 50 bold",bg="white")
clock.grid(row=2,column=2)
# Calling funtion to show time
showTime()

digi = Label(root, text="Digital Clock",font="times 24 bold")
digi.grid(row=1,column=2)

notation = Label(root,text="Hours   Minutes    Seconds")
notation.grid(row=3,column=2)

root.mainloop()
