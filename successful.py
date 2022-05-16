from tkinter import *
from tkinter import StringVar
from typing import Type
root = Tk()

#size of the window
root.geometry("500x300")
#icon photo for logo
root.iconbitmap(':financialstudies$/Desktop/banderalogo.png')

#this is the color of the background
root["bg"] = "light blue"

#this allows the window to terminate after the user selects exit
def close():
    root.destroy()

#informs the user their registration was successful
Label(root, text="Bandera Entertainment Registration Successful!", font="arial 15 bold").grid(row=0, column=3)

#this is the exit button
Button(text="Exit" , command=close).grid(row=4, column=3)

root.mainloop()
