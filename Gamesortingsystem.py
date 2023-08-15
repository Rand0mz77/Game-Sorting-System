from tkinter import *
from functools import partial
import csv

#Opens a new window to add games

def AddScreen():
   global AddEntry
   addscreen = Tk()
   addscreen.configure(width=250, height=250)
   AddEntry = Entry(addscreen).place(x=75, y=75)
   AddButton = Button(addscreen, text = "Add", command = AddScreen).place(x = 95, y = 95)

   with open('game_file.csv', mode='a') as game_file:

      game_writer = csv.writer(game_file, delimiter=',')

      game_writer.writerow([AddEntry.get()])
   
#Opens a new window to remove games

def RemoveScreen():
   removescreen = Tk()
   removescreen.configure(width=750, height=500, bg='LavenderBlush')

#Opens a new window to search for games

def SearchScreen():
   searchscreen = Tk()
   searchscreen.configure(width=750, height=500, bg='LavenderBlush')

#Once Log-in button is pressed it will open the UI for the games

def validateLogin(username, password):
   global tkwindow1
   if username.get() == "CalebBorg" and password.get() == "123":
      tkwindow1 = Tk()
      tkwindow1.configure(width=750, height=500, bg='LavenderBlush')
      title1_label = Label(tkwindow1, text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'LavenderBlush').place(x =250, y = 25)
      add_button = Button(tkwindow1, text = 'Add', command=AddScreen).place(x = 100, y = 100)
      remove_button = Button(tkwindow1, text = 'Remove', command=RemoveScreen).place(x = 100, y = 150)
      search_button = Button(tkwindow1, text = 'Search', command=SearchScreen).place(x = 100, y = 200)
      LogOut_button = Button(tkwindow1, text = 'Log Out', bg='Red', fg='White', command=Logout).place(x = 675, y = 465)
      tkwindow.withdraw()
   else:
      error_label = Label(tkwindow, text = 'Username and Password Incorrect', fg = 'Red', bg = 'LavenderBlush').place(x = 280, y = 350)

#Allows user to log-out

def Logout():
   tkwindow.deiconify()
   tkwindow1.withdraw()

#Opens window

tkwindow = Tk()
tkwindow.configure(width=750, height=500, bg='LavenderBlush')

#Shows title

title_label = Label(text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'LavenderBlush').place(x =250, y = 25)

#Username label & entry box

username_label = Label(tkwindow, text = 'Username', font = ('Arial', 16), fg = 'black', bg = 'LavenderBlush').place(x = 325, y = 100)
username = StringVar()
usernameEntry = Entry(font=('Verdana', 16), width=10, textvariable = username).place(x =315, y = 150)

#Password label & entry box

password_label = Label(tkwindow, text = 'Password', font = ('Arial', 16), fg = 'black', bg = 'LavenderBlush').place(x = 325, y = 200)
password = StringVar()
passwordEntry = Entry(font=('Verdana', 16), width=10, textvariable = password, show = '*').place(x = 315, y = 250)

validateLogin = partial(validateLogin, username, password)

#Log-in button

login_button = Button(text='Enter', font=('Arial', 10), command=validateLogin).place(x = 350, y = 300)

#Loops the code to make a permenant window

mainloop()