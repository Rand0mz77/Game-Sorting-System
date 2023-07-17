from tkinter import *

window = Tk()
window.configure(width=750, height=500)
window.configure(bg='#494444')

def login():
    username = "makeuseof"
    password = "muo"

    if username_label.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

title_label = Label(text = 'Video Game Sorting System', font = ('Gotham', 16), fg = 'black', bg = 'light gray')
username_label = Label(text = 'Username', font = ('Arial', 16), fg = 'black', bg = 'light gray')
password_label = Label(text = 'Password', font = ('Arial', 16), fg = 'black', bg = 'light gray')

login_button = Button(text='Enter', font=('Arial', 10),command=login)

entry = Entry(font=('Verdana', 16), width=10)
entry2 = Entry(font=('Verdana', 16), width=10)

title_label.place(x =250, y = 25)
username_label.place(x = 325, y = 100)
password_label.place(x = 325, y = 200)
entry.place(x =315, y = 150)
entry2.place(x =315, y = 250)
login_button.place(x = 315, y = 300)
mainloop()