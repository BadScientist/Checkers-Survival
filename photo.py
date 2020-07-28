from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont

import os

root = Tk()

root.config(bg='#3b444b')


root.geometry('900x700') 

#this clears out the text in the text box for username
def clear_username1(event):
    username1.delete(0, END)

def clear_name1(event):
    name1.delete(0, END)

def clear_password1(event):
    password1.delete(0, END)

def clear_username2(event):
    username2.delete(0, END)

def clear_password2(event):
    password2.delete(0, END)



#Title
title = Label(root, text="Crashed",font=("Courier" ,54), pady=70, fg='white', bg='#3b444b')
title.pack() 

frame1 = Frame(root, width=350, height=200, bg='#3b444b')
frame2 = Frame(root, width=350, height=200, bg='#3b444b')
frame3 = Frame(root, width=350, height=200, bg='#3b444b')
frame4 = Frame(root, width=350, height=200, bg='#3b444b')

###USERNAME LEFT PART###
pic1 = Image.open('username.png')
resize1 = pic1.resize((30,30), Image.ANTIALIAS)
username_img = ImageTk.PhotoImage(resize1)
u_img = Label(frame1, image=username_img)
u_img.config(bg='#3b444b')
u_img.pack(side=LEFT, anchor= "nw") 

#username entry box is here
username1 = Entry(frame1, width=25)
username1.insert(0, "Username") 
username1.pack(side= LEFT, anchor= "nw", pady= 10, padx= 5)
username1.bind("<Button-1>", clear_username1)
###LOGIN USERNAME END###

###NAME RIGHT PART###
pic3 = Image.open('name.png')
resize3 = pic3.resize((30,30), Image.ANTIALIAS)
username_img3 = ImageTk.PhotoImage(resize3)
u_img3 = Label(frame1, image=username_img3)
u_img3.config(bg='#3b444b')
u_img3.pack(side= LEFT, anchor= "nw", padx= (150, 0)) 

#name entry box is here
name1 = Entry(frame1, width=25)
name1.insert(0, "Name")
name1.pack(side= LEFT, anchor= "nw", pady= 10, padx= 5)
name1.bind("<Button-1>", clear_name1)
###NAME END###

###PASSWORD LEFT PART###
pic2 = Image.open('password.png')
resize2 = pic2.resize((30,30), Image.ANTIALIAS)
username_img2 = ImageTk.PhotoImage(resize2)
u_img2 = Label(frame2, image=username_img2)
u_img2.config(bg='#3b444b')
u_img2.pack(side=LEFT, anchor= "nw") 

#password for the login part 
password1 = Entry(frame2, width=25)
password1.insert(0, "Password")
password1.pack(side= LEFT, anchor= "nw", pady= 10, padx= 5)
password1.bind("<Button-1>", clear_password1)
###Pasword END###

###USERNAME PART###
pic4 = Image.open('username.png')
resize4 = pic4.resize((30,30), Image.ANTIALIAS)
username_img4 = ImageTk.PhotoImage(resize4)
u_img4 = Label(frame2, image=username_img4)
u_img4.config(bg='#3b444b')
u_img4.pack(side= LEFT, anchor= "nw", padx= (150, 0)) 

#username entry box is here
username2 = Entry(frame2, width=25)
username2.insert(0, "Username")
username2.pack(side= LEFT, anchor= "nw", pady= 10, padx= 5)
username2.bind("<Button-1>", clear_username2)
###USERNAME END###


#button for the login part
blank = Label(frame3, text="", bg='#3b444b')
blank.pack(side=LEFT, anchor= "nw", padx=(45,0))
button = Button(frame3, text="Login",bg="#FF0000", fg='white', width= 15, padx= 10)
button.pack(side=LEFT, anchor= "nw")

###PASSWORD PART###
pic5 = Image.open('password.png')
resize5 = pic5.resize((30,30), Image.ANTIALIAS)
username_img5 = ImageTk.PhotoImage(resize5)
u_img5 = Label(frame3, image=username_img5)
u_img5.config(bg='#3b444b')
u_img5.pack(side= LEFT, anchor= "nw", padx= (164, 0))  

#password for the login part 
password2 = Entry(frame3, width=25)
password2.insert(0, "Password")
password2.pack(side= LEFT, anchor= "nw", pady= 10, padx= 5)
password2.bind("<Button-1>", clear_password2)
###PASSWORD END###

#button for the login part
random = Label(frame4, text="", bg='#3b444b')
random.pack(side=LEFT, anchor= "nw", padx=(100,0))
button1 = Button(frame4, text="Sign Up", bg="#FF0000", fg='white', width= 18)
button1.pack(side=LEFT, anchor= "nw", padx=(275,0))



frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()


root.mainloop()
