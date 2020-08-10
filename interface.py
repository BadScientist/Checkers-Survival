from player import *
from tkinter import *
from mapGUI import start_mini_map_IO
import tkinter.font as tkFont
import math

'''
Changes:
    The player is initialized via passing the UI canvas ie canvas1 to player
    class.
    The UI can then be modified from there.
    ********* Note: you can only call it once every element of canvas1 has been
                    initialized.
    see bottom of Game Settings for example
        
How to Print to the UI from interface.py:
    pass string to print prompt below canvas1 definitions.
'''

#TODO: Keep refreshing and reprinting the:
    #   1. Health
    #   2. Time
    #   3. Inventory

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

def new_game():
    f10.pack()
    title.pack_forget()
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()

    print("Start New Game")

def load_game():
    print("Load Old Game") 

def info():
    f5.pack()
    f4.pack_forget()

def info_back():
    f4.pack()
    f5.pack_forget()

def settings():
    f6.pack()
    f4.pack_forget()

def settings_back():
    f4.pack()
    f6.pack_forget() 

def help5():
    f7.pack()
    f4.pack_forget()

def help_back():
    f4.pack()
    f7.pack_forget()

###END Page Switches###

###Frames###
f1 = Frame(root, bg='#3b444b')
f2 = Frame(root, bg='#3b444b')
f3 = Frame(root, bg='#3b444b')
f4 = Frame(root, bg='#3b444b')
f5 = Frame(root, bg='#3b444b')
f6 = Frame(root, bg='#3b444b')
f7 = Frame(root, bg='#3b444b')
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

button = Button(frame2, text="Exit",bg='#FF0000', fg='white',width= 15, command=root.destroy)
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

button = Button(frame0, text="New Game",bg='#cc5500', fg='white',width= 15, command=new_game)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame1, text="Load Game",bg='#cc5500', fg='white',width= 15, command=load_game)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame2, text="Info",bg='#cc5500', fg='white',width= 15, command=info)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame3, text="Help",bg='#cc5500', fg='white',width= 15, command=help5)
button.pack(side=LEFT, anchor= "nw")

button = Button(frame4, text="Settings",bg='#cc5500', fg='white',width= 15, command=settings)
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

###Info Tab###
c1 = Canvas(f5, bg='#5a6873', width=500, height=400)

#the info tab and the underline part
font1 = tkFont.Font(family="Courier",size=13,weight="bold")
c1.create_text(30, 20, text="Info:", font=font1, fill='white')

#info goes here
c1.create_text(250, 50, text="Disaster! Once assigned the prestigious task of establishing a Research Outpost orbiting", fill='white')
c1.create_text(250, 65, text="Earth to study the technologically rudimentary humanoids, a mechanical failure rendered", fill='white')
c1.create_text(250, 80, text="you unable to reach a stable orbit over the planet. You had no choice but to enter the", fill='white')
c1.create_text(250, 95, text="planet's rich atmosphere and crash landed on one of it's islands. Nonetheless, protocol", fill='white')
c1.create_text(250, 110, text="dictates that radio silence for a period of 5 rotations (5 days) will necessitate a ", fill='white')
c1.create_text(250, 125, text="search-and-rescue mission to be dispatched. Hunt, Work with friendly natives, Brave the", fill='white')
c1.create_text(250, 140, text="planet's hazards - but by all means... Survive.", fill='white')

#back button 
button = Button(c1, text="Back",bg='#cc5500', fg='white', width= 15, command=info_back)
button.pack()
c1.create_window(75, 375, window=button)

c1.pack()

###End Info Tab###

###Settings Tab###
c3 = Canvas(f6, bg='#5a6873', width=500, height=400)

#title for settings
font1 = tkFont.Font(family="Courier",size=13,weight="bold")
c3.create_text(50, 20, text="Settings:", font=font1, fill='white')

#settings options
font2 = tkFont.Font(family="Courier",size=10)

c3.create_text(200, 40, text="---", font=font2,fill='white')
set1 = Checkbutton(c3, bg='#5a6873')
c3.create_window(230, 40,window=set1)


#back button
button = Button(c3, text="Back",bg='#cc5500', fg='white', width= 15, command=settings_back)
button.pack()
c3.create_window(75, 375, window=button)

#update button 
button = Button(c3, text="Update",bg='#cc5500', fg='white', width= 15)
button.pack()
c3.create_window(425, 375, window=button)

c3.pack()

###End Settings Tab###

###Help Tab###
c2 = Canvas(f7, bg='#5a6873', width=500, height=400)

#the info tab and the underline part
font1 = tkFont.Font(family="Courier",size=13,weight="bold")
c2.create_text(30, 20, text="Help:", font=font1, fill='white')

#title and box
font2 = tkFont.Font(family="Courier",size=10)
c2.create_text(90, 50, text="Title:", font=font2, fill='white')

box1 = Entry(c2, width=50)
box1.pack()

c2.create_window(275, 50, window=box1)
#descrip and box
c2.create_text(65, 75, text="Description:", font=font2, fill='white')

box2 = Entry(c2, width=50)
box2.pack()

c2.create_window(275, 75, window=box2)


#back button
button = Button(c2, text="Back",bg='#cc5500', fg='white', width= 15, command=help_back)
button.pack()
c2.create_window(75, 375, window=button)

#submit button
button = Button(c2, text="Submit",bg='#cc5500', fg='white', width= 15)
button.pack()
c2.create_window(425, 375, window=button)

c2.pack()

###End Help Tab###


#############################################################################
###GAME INTERFACE###
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func    

#changes the color of the score
def healthcolor():
    score = healthScore()
    
    if score == 100:
        return "Green"
    elif 90 > score > 40:
        return "Black"
    else:
        return "Red"

#this will be where the score is optained
def healthScore():
    return player._health

#grabs the day
def specDay():
    day = 1
    #this will be where it grabs the day
    return day

#we will have to talk to see what we want to do abou this feature
def clock():
    time= "00:00"

    return time

#how many health packs the user has
def hpNumber():
    hp = 0 
    i = 0
    # for D in player._inventory:
    #     # if player._inventory[i] == "MEDPACK":
    #     #     hp += 1
    #     #     break
    #     i +=1
    return hp

#how much meat the user has
def meatNumber():
    meat = 0
    return meat

#the amount of hunting knifes the user has
def hkNumber():
    hk = 0
    return hk

#this will be where it figures out what the text says
def searchDirection():
    result = entry10.get()
    player.get_user_input(cur_level, result)
    entry10.delete(0, END)

    if player.get_location().get_next_level() == True:
        prompt_move_nxt_level()

    midright.destroy()
    newMiniMap()

#this refreshes the mini map in the corner
def newMiniMap():
    midright = Canvas(canvas1, bg="#bbbbbb", width=290, height=290,highlightthickness=3, highlightbackground="black")
    start_mini_map_IO(midright, player.location)

    midright.pack()
    canvas1.create_window(730, 230, window=midright)

#Directly prints a prompt to the dialog box to the left
def print_prompt(value):
    dialogleft = Canvas(canvas1, bg="#bbbbbb",width=550, height=600, highlightthickness=3, highlightbackground="black")
    prompt = Text(dialogleft, height=35, width=65, bg="#bbbbbb", highlightthickness=0)
    prompt.insert(END, value)
    dialogleft.pack()
    prompt.pack()
    canvas1.create_window(300, 325, window=dialogleft)

def identify_start_room(level):
    #returns room with greatest distance from nxt_lvl event ie start_room
    for room in level:
        if room.get_next_level() == True:
            nxt_lvl_room = room
            break
    nxt_lvl_position = nxt_lvl_room.get_position()
    
    #use below as standard in case there is only 1 room in level.
    #otherwise it is bound to change
    max_distance = 0
    start_room = nxt_lvl_room 
    
    for room in set(level) - {nxt_lvl_room}:
        room_position = room.get_position()
        distance = math.hypot(nxt_lvl_position[0]-room_position[0],
                              nxt_lvl_position[1]-room_position[1])
        if distance > max_distance:
            max_distance = distance
            start_room = room
    return start_room

#handles the transition between levels
def transition_new_level():
    #FIXME: find a way to work without globals
    #TODO: way of destroying or quitting once game is over
    global cur_level, level_idx, player
    level_idx+=1
    
    if level_idx < len(levels):
        new_level = levels[level_idx]
    else: #if all levels are complete
        new_level = None
    
    if new_level == None: #all levels complete
        print_prompt('All Levels Complete')
        #root.destroy()
    elif new_level != cur_level:
        cur_level = new_level
        player.set_start_position(identify_start_room(cur_level))

#prompt user whether they want to move to the next level
def prompt_move_nxt_level():
    #Returns either True/False
    response = Tk(className=" Progression")
    response.config(bg='#3b444b')
    title = Label(response, text='Advance to the next level?', pady=30,
                  font=("Courier",12), fg='white', bg='#3b444b')
    Yes = Button(response, text="Yes", padx=30, pady=5,
                 command=combine_funcs(transition_new_level,response.destroy,
                                       midright.destroy, newMiniMap),
                 bg='#cc5500', fg='white', highlightthickness=0)
    No = Button(response, text="No", padx=30, pady=5, command=response.destroy,
                bg='#cc5500', fg='white', highlightthickness=0)
    title.grid(row=0, columnspan=2)
    Yes.grid(row=1, column=0)
    No.grid(row=1, column=1)
    
#GAME SETTINGS

###Frames###
f10 = Frame(root, bg='#3b444b')
###End Frames
canvas1 = Canvas(f10, bg='#3b444b', width=900, height=700)

level_size = [10, 12, 15, 18, 23]
levels = [
    gen_random_level(level_size[0], 1),
    gen_random_level(level_size[1], 2),
    gen_random_level(level_size[2], 3),
    gen_random_level(level_size[3], 4),
    gen_random_level(level_size[4], 5),
]

# Initialize first Level and Player
level_idx = 0
cur_level = levels[level_idx]
player = Player(canvas1)
player.set_start_position(identify_start_room(cur_level))

#font for texts on screen
font2 = tkFont.Font(family="Courier",size=13, weight="bold")

#dialog box on the left
dialogleft = Canvas(canvas1, bg="#bbbbbb",width=550, height= 600, highlightthickness=3, highlightbackground="black")
dialogleft.pack()
canvas1.create_window(300, 325, window=dialogleft)

#the box you can type on on the bottom right
textbox= Canvas(canvas1, bg="white", width=550, height=40, highlightthickness=3, highlightbackground="black")

textbox.create_text(15, 23, text=">", font=font2, fill="black")
entry10 = Entry(textbox, width=65) #this is the entry box
entry10.pack()
textbox.create_window(230, 23, window=entry10) #packing the entry box

textbox_button = Button(textbox, text="Submit", bg='#cc5500', fg='white', height=2, width=15, command=searchDirection) #new button for submit
textbox_button.pack()
textbox.create_window(496, 23, window=textbox_button) #pack the box

textbox.pack()
canvas1.create_window(300, 660, window=textbox)

#top right health and day box
topright = Canvas(canvas1, bg="#bbbbbb", width=290, height=50, highlightthickness=3, highlightbackground="black")

topright.create_text(43, 27, text="Health ", font=font2, fill="black")
topright.create_text(90, 27, text= healthScore(), font=font2, fill= healthcolor()) #this will be the changable variable for health also color changes for health
topright.create_text(125, 27, text="/100", font=font2, fill="black")

topright.create_text(195, 27, text="Day ", font=font2, fill="black")
topright.create_text(218, 27, text= specDay(), font=font2, fill= "black")
topright.create_text(227, 27, text=",", font=font2, fill="black")

topright.create_text(260, 27, text= clock(), font=font2, fill= "black")


topright.pack()
canvas1.create_window(730, 50, window=topright)

#map box middle right
midright = Canvas(canvas1, bg="#bbbbbb", width=290, height=290,highlightthickness=3, highlightbackground="black")

start_mini_map_IO(midright, player.location)

midright.pack()
canvas1.create_window(730, 230, window=midright)

#inventory box bottom right
botright = Canvas(canvas1, bg="#bbbbbb", width=290, height=295, highlightthickness=3, highlightbackground="black")

botright.create_text(60, 27, text="Health Pack", font=font2, fill="black")
botright.create_text(27, 47, text="Meat", font=font2, fill="black")
botright.create_text(75, 67, text="Hunting Knife ", font=font2, fill="black")

botright.create_text(275, 27, text=hpNumber(), font=font2, fill="black")
botright.create_text(275, 47, text=meatNumber(), font=font2, fill="black")
botright.create_text(275, 67, text=hkNumber(), font=font2, fill="black")

botright.pack()
canvas1.create_window(730, 533, window=botright)

canvas1.pack()

#********Examples of how we can print to UI*************
# print_prompt('sbclkhjsbdcj bisub o;s')
# player.print_prompt('uhbcibw')
#*************************************

#f10.pack()


###END GAME INTERFACE###
#############################################################################

f1.pack()
f6.pack_forget()
root.mainloop()