from tkinter import *
from functools import partial
import csv
   
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

def showmainmenu():
   global tkwindow1
   global addentry
   global removeentry 


   tkwindow1 = Tk()
   tkwindow1.configure(width=1500, height=750, bg='LavenderBlush')

   title1label = Label(tkwindow1, text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'LavenderBlush')
   title1label.place(x =250, y = 25)

   title2label = Label(tkwindow1, text = 'By Troy Pool', font = ('Gotham', 8), fg = 'Light Gray', bg = 'LavenderBlush')
   title2label.place(x = 350, y = 50)

   gamestextbox = Text(tkwindow1, wrap=WORD, width = 75, height = 25)
   gamestextbox.place(x = 350, y= 75)
   with open("Games.txt", "r") as games:
      gamestextbox.insert(INSERT, games.read())
      gamestextbox.config(state=DISABLED)

   addbutton = Button(tkwindow1, text = 'Add', command=lambda:[AddGame()])
   addbutton.place(x = 100, y = 100)


   addentry = Entry(tkwindow1)
   addentry.place(x = 100, y = 150)

   removebutton = Button(tkwindow1, text = 'Remove', command = lambda:[RemoveGame()])
   removebutton.place(x = 100, y = 200)

   removeentry = Entry(tkwindow1)
   removeentry.place(x = 100, y = 250)

   searchbutton = Button(tkwindow1, text = 'Search')
   searchbutton.place(x = 100, y = 300)

   searchentry = Entry(tkwindow1)
   searchentry.place(x = 100, y = 350)

   LogOutbutton = Button(tkwindow1, text = 'Log Out', bg='Red', fg='White', command=Logout)
   LogOutbutton.place(x = 675, y = 650)

   tkwindow.withdraw()

def ReturnGame():
   return addentry

def AddGame():
   Gamesfile=open("Games.txt", "a")
   Gamesfile.write(addentry.get())
   Gamesfile.write("\n")

def RemoveGame():
   with open("Games.txt", "r") as file:
      lines = file.readlines()
   with open("Games.txt", "w") as file:
      for line in lines:
         if line.strip() != removeentry.get():
            file.write(line)




def Logout():
   tkwindow.deiconify()
   tkwindow1.withdraw()

#Opens window

tkwindow = Tk()
tkwindow.configure(width=750, height=500, bg='LavenderBlush')

#Shows title

titlelabel = Label(text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'LavenderBlush').place(x =250, y = 25)

#Username label & entry box

usernamelabel = Label(tkwindow, text = 'Username', font = ('Arial', 16), fg = 'black', bg = 'LavenderBlush').place(x = 325, y = 100)
username = StringVar()
usernameEntry = Entry(font=('Verdana', 16), width=10, textvariable = username).place(x =315, y = 150)

#Password label & entry box

passwordlabel = Label(tkwindow, text = 'Password', font = ('Arial', 16), fg = 'black', bg = 'LavenderBlush').place(x = 325, y = 200)
password = StringVar()
passwordEntry = Entry(font=('Verdana', 16), width=10, textvariable = password, show = '*').place(x = 315, y = 250)

validateLogin = partial(validateLogin, username, password)

#Log-in button

loginbutton = Button(text='Enter', font=('Arial', 10), command=validateLogin).place(x = 350, y = 300)

#Loops the code to make a permenant window

mainloop()