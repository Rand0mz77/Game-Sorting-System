from tkinter import *
from functools import partial
import csv
import time
   
#Once Log-in button is pressed it will open the UI for the games

def validateLogin(username, password):
   global tkwindow1
   global addentry
   if username.get() == "1" and password.get() == "1":
      showmainmenu()
      print("Login Succesful")

   else:
      errorlabel = Label(tkwindow, text = 'Username and Password Incorrect', fg = 'Red', bg = 'LavenderBlush').place(x = 280, y = 350)
      errorlabel.place(x = 280, y = 350)
#Shows Main Menu

def showmainmenu():
   global tkwindow1
   global addentry
   global removeentry 

   tkwindow1 = Tk()
   tkwindow1.configure(width=1500, height=750, bg='LavenderBlush')

   #Title label

   title1label = Label(tkwindow1, text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'LavenderBlush')
   title1label.place(x =250, y = 25)

   #Author Label

   title2label = Label(tkwindow1, text = 'By Troy Pool', font = ('Gotham', 8), fg = 'Light Gray', bg = 'LavenderBlush')
   title2label.place(x = 350, y = 50)

   #Add button

   addbutton = Button(tkwindow1, text = 'Add', command=lambda:[AddGame()])
   addbutton.place(x = 100, y = 100)

   #Add entry box

   addentry = Entry(tkwindow1)
   addentry.place(x = 100, y = 150)

   #Remove button

   removebutton = Button(tkwindow1, text = 'Remove', command = lambda:[RemoveGame()])
   removebutton.place(x = 100, y = 200)

   #Remove entry box

   removeentry = Entry(tkwindow1)
   removeentry.place(x = 100, y = 250)

   #Search Button

   searchbutton = Button(tkwindow1, text = 'Browse', command = searchmenu)
   searchbutton.place(x = 100, y = 300)

   #Log-out button

   LogOutbutton = Button(tkwindow1, text = 'Log Out', bg='Red', fg='White', command=lambda:[Logout(), cleartext()])
   LogOutbutton.place(x = 675, y = 650)

   tkwindow.withdraw()

def ReturnGame():
   return addentry

#Allows the user to add games

def AddGame():
   Gamesfile=open("Games.txt", "a")
   Gamesfile.write(addentry.get())
   Gamesfile.write("\n")

#Allows the user to remove games

def RemoveGame():
   with open("Games.txt", "r") as file:
      lines = file.readlines()
   with open("Games.txt", "w") as file:
      for line in lines:
         if line.strip() != removeentry.get():
            file.write(line)

#Allows the user to search and browse games

def searchmenu():
   tkwindow2 = Tk()
   tkwindow2.configure(width = 500, height = 500, bg = 'LavenderBlush')
   gamestextbox = Text(tkwindow2, wrap=WORD, width = 50, height = 25)
   gamestextbox.place(x = 50, y= 50)
   with open("Games.txt", "r") as games:
      gamestextbox.insert(INSERT, games.read())
      gamestextbox.config(state=DISABLED)

#Allows user to log-out

def cleartext():
   usernameEntry.delete(0, END)
   passwordEntry.delete(0, END)

def Logout():
   tkwindow.deiconify()
   tkwindow1.withdraw()      

global usernameEntry
global passwordEntry

#Opens Log-in window

tkwindow = Tk()
tkwindow.configure(width=750, height=500, bg='LavenderBlush')

#Shows title

titlelabel = Label(text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'LavenderBlush').place(x =250, y = 25)

#Username label & entry box

usernamelabel = Label(tkwindow, text = 'Username', font = ('Arial', 16), fg = 'black', bg = 'LavenderBlush').place(x = 325, y = 100)
username = StringVar()
usernameEntry = Entry(font=('Verdana', 16), width=10, textvariable = username)
usernameEntry.place(x =315, y = 150)

#Password label & entry box

passwordlabel = Label(tkwindow, text = 'Password', font = ('Arial', 16), fg = 'black', bg = 'LavenderBlush').place(x = 325, y = 200)
password = StringVar()
passwordEntry = Entry(font=('Verdana', 16), width=10, textvariable = password, show = '*')
passwordEntry.place(x = 315, y = 250)

validateLogin = partial(validateLogin, username, password)

#Log-in button

loginbutton = Button(text='Enter', font=('Arial', 10), command=validateLogin).place(x = 350, y = 300)

#Loops the code to make a permenant window

mainloop()