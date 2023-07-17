from tkinter import *

def validateLogin():
    username = "use"
    password = "pas"
    return

#Opens window
tkwindow = Tk()
tkwindow.configure(width=750, height=500)
tkwindow.configure(bg='#494444')
#Shows title
title_label = Label(text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'light gray').place(x =250, y = 25)
#Username label & entry box
username_label = Label(tkwindow, text = 'Username', font = ('Arial', 16), fg = 'black', bg = 'light gray').place(x = 325, y = 100)
username = StringVar()
usernameEntry = Entry(font=('Verdana', 16), width=10, textvariable = username).place(x =315, y = 150)
#Password label & entry box
password_label = Label(tkwindow, text = 'Password', font = ('Arial', 16), fg = 'black', bg = 'light gray').place(x = 325, y = 200)
password = StringVar()
passwordEntry = Entry(font=('Verdana', 16), width=10, textvariable = password, show = '*').place(x = 315, y = 250)

#Log-in button
login_button = Button(text='Enter', font=('Arial', 10)).place(x = 350, y = 300)
#Loops the code to make a permenant window
mainloop()