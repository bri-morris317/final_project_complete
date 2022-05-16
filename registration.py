from tkinter import *
from tkinter import StringVar

ws = Tk()
#determines the size of the window
ws.geometry("500x300")
#adds the icon in the window
ws.iconbitmap(':financialstudies$/Desktop/banderalogo.png')

#connects to the final page after the user registers.
def nextPage():
    ws.destroy()
    import successful.py

#this allows the user to go back to the previous page
def previousPage():
    ws.destroy()
    import home.py


# Creating Labels
Label(ws, text="Bandera Entertainment Registration", font="arial 15 bold").grid(row=0, column=3)
firstName = Label(ws, text="First Name")
lastName = Label(ws, text="Last Name")
email = Label(ws, text="Email")
favoriteShow = Label(ws, text="Favorite Show")
favoriteCharacter = Label(ws, text="Favorite Character")

# Packing Fields
firstName.grid(row=1, column=2)
lastName.grid(row=2, column=2)
email.grid(row=3, column=2)
favoriteShow.grid(row=4, column=2)
favoriteCharacter.grid(row=5, column=2)

# Variables for storing data
firstNameValue = type[StringVar]
lastNameValue = type[StringVar]
emailValue = type[StringVar]
favoriteShowValue = type[StringVar]
favoriteCharacterValue = type[StringVar]
checkValue = IntVar

# Creating Entry Field for Users
firstNameEntry = Entry(ws, textvariable=firstNameValue)
lastNameEntry = Entry(ws, textvariable=lastNameValue)
emailEntry = Entry(ws, textvariable=emailValue)
favoriteShowEntry = Entry(ws, textvariable=favoriteShowValue)
favoriteCharacterEntry = Entry(ws, textvariable=favoriteCharacterValue)

# Packing Entry Fields for Users
firstNameEntry.grid(row=1, column=3)
lastNameEntry.grid(row=2, column=3)
emailEntry.grid(row=3, column=3)
favoriteShowEntry.grid(row=4, column=3)
favoriteCharacterEntry.grid(row=5, column=3)

# Submit Button
Button(text="Submit", command=nextPage).grid(row=6, column=3)
Button(text="Go Back", command=previousPage).grid(row=7, column=3)

ws.mainloop()
