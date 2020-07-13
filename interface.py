from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from PIL import Image, ImageTk

import os

root = Tk()


###Page Setup###
root.config(bg='#3b444b')
root.geometry('900x700') 

###END Page Setup###

###Page Switches###
def login_page():
    f2.pack()
    f1.pack_forget()

def signup_page():
    f3.pack()
    f1.pack_forget()

def login_back():
    f1.pack()
    f2.pack_forget()

def signup_back():
    f1.pack()
    f3.pack_forget()

def start_game():
    f4.pack()
    f1.pack_forget()
    f3.pack_forget()
    f2.pack_forget()

def back_menu():
    f1.pack()
    f4.pack_forget()


###END Page Switches###

###Frames###
f1 = Frame(root, bg='#3b444b')
f2 = Frame(root, bg='#3b444b')
f3 = Frame(root, bg='#3b444b')
f4 = Frame(root, bg='#3b444b')
###END Frames###

title = Label(root, text="Crashed",font=("Courier" ,54), pady=70, fg='white', bg='#3b444b')
title.pack() 

###Main Page###
frame0 = Frame(f1, bg='#3b444b' ,pady=5)
frame1 = Frame(f1)
frame2 = Frame(f1, bg='#3b444b' ,pady=5)

button = Button(frame0, text="Login",bg='#cc5500', fg='white',width= 15, command=login_page)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame1, text="Signup",bg='#cc5500', fg='white',width= 15, command=signup_page)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame2, text="Exit",bg='#FF0000', fg='white',width= 15, command=root.quit)
button.pack(side=LEFT, anchor= "nw")

frame0.pack()
frame1.pack()
frame2.pack()
###END Main Page###

###Login Page###
#this clears out the text in the text box for username
def clear_username1(event):
    username2.delete(0, END)

def clear_password1(event):
    password2.delete(0, END)

frame1 = Frame(f2, bg='#3b444b' ,pady=10)
frame2 = Frame(f2)
frame3 = Frame(f2, bg='#3b444b' ,pady=10)

#username entry box is here
username2 = Entry(frame1, width=25)
username2.insert(0, "Username") 
username2.pack(side=LEFT, anchor= "nw")
username2.bind("<Button-1>", clear_username1)
###LOGIN USERNAME END###

#password for the login part 
password2 = Entry(frame2, width=25)
password2.insert(0, "Password")
password2.pack(side=LEFT, anchor= "nw")
password2.bind("<Button-1>", clear_password1)
###Pasword END###

button = Button(frame3, text="Back",bg='#cc5500', fg='white', width= 15, command=login_back)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame3, text="Login",bg='#cc5500', fg='white',width= 15, command=start_game)
button.pack(side=LEFT, anchor= "nw")

frame1.pack()
frame2.pack()
frame3.pack()
###END Login Page

###Sign Up Page###
#this clears out the text in the text box for username
def clear_username2(event):
    username1.delete(0, END)

def clear_password2(event):
    password1.delete(0, END)

def clear_name1(event):
    name1.delete(0, END)

frame0 = Frame(f3, bg='#3b444b' ,pady=10)
frame1 = Frame(f3, bg='red')
frame2 = Frame(f3, bg='#3b444b' ,pady=10)
frame3 = Frame(f3, bg='yellow')

#name entry box is here
name1 = Entry(frame0, width=25)
name1.insert(0, "Name")
name1.pack(side= LEFT, anchor= "nw")
name1.bind("<Button-1>", clear_name1)
###NAME END###

#username entry box is here
username1 = Entry(frame1, width=25)
username1.insert(0, "Username") 
username1.pack(side=LEFT, anchor= "nw")
username1.bind("<Button-1>", clear_username2)
###LOGIN USERNAME END###

#password for the login part 
password1 = Entry(frame2, width=25)
password1.insert(0, "Password")
password1.pack(side=LEFT, anchor= "nw")
password1.bind("<Button-1>", clear_password2)
###Pasword END###

button = Button(frame3, text="Back",bg='#cc5500', fg='white', width= 15, command=signup_back)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame3, text="Signup",bg='#cc5500', fg='white',width= 15, command=start_game)
button.pack(side=LEFT, anchor= "nw")

frame0.pack()
frame1.pack()
frame2.pack()
frame3.pack()
###End Sign Up Page###

###Menu###
frame0 = Frame(f4, bg='#3b444b' ,pady=5)
frame1 = Frame(f4, bg='red')
frame2 = Frame(f4, bg='#3b444b' ,pady=5)
frame3 = Frame(f4, bg='yellow')
frame4 = Frame(f4, bg='#3b444b' ,pady=5)
frame5 = Frame(f4, bg='yellow')

button = Button(frame0, text="New Game",bg='#cc5500', fg='white',width= 15)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame1, text="Load Game",bg='#cc5500', fg='white',width= 15)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame2, text="Info",bg='#cc5500', fg='white',width= 15)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame3, text="Help",bg='#cc5500', fg='white',width= 15)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame4, text="Settings",bg='#cc5500', fg='white',width= 15)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame5, text="Log Out",bg="#FF0000", fg='white',width= 15, command=back_menu)
button.pack(side=LEFT, anchor= "nw")

frame0.pack()
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()

###END Menu###

f1.pack()
root.mainloop()
