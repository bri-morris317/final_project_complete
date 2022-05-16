#allows for import to create in tkinter
from tkinter import *
from tkinter import StringVar
from typing import Type

ws = Tk()
#determines the size of the window
ws.geometry("500x300")
#the icon on the window next to the letters tk
ws.iconbitmap(':financialstudies$/Desktop/banderalogo.png')

#this is the text and size for the heading of the registration page
Label(ws, text="Bandera Entertainment Registration", font="arial 15 bold").grid(row=0, column=1)
#this is for the label asking user if they want to sign up
sign = Label(ws, text="Ready to Sign Up? Click Below!")

sign.grid(row=1, column =1)

#this connects the registration page and terminates the current window after opening
def nextPage():
    ws.destroy()
    import registration.py


# Submit Button
Button(text="Sign Up!" , command=nextPage,).grid(row=2, column=1)


ws.mainloop()
