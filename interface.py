from player import *
from tkinter import *
from mapGUI import start_mini_map_IO
import tkinter.font as tkFont
import math

'''
    for implementing load game method:
    
There's a simple if statement which uses load_save like a flag.
if user selects load game, the load_save variable is set to True

if load_save is true when the player & map are being created, if statement will
overwrite the newly created player and will load the database data to the
player object

its a poor method, I know. Pls change if you have another implementation
'''


# TODO: - create save game button and methods
#       - load save game (from database) - see load_save variable below under
#         Game Info, and the if statement under 'Game Variables' section to
#         place your code

# FIXME: level_transitions list is missing

root = Tk()

# # #Page Setup# # #
root.config(bg='#3b444b')
root.geometry('900x700') 

# # #END Page Setup# # #


# Game info:
#   (for now, its only if the game is loaded or not).
#   you can even set this as a dict should you like
'''
    var load_save: whether the game should be loaded (True) or not (False)
'''
load_save = False  # default to create a new game


# # #Page Switches# # #
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

    print_prompt("Crashed\n\nDisaster! Once assigned the prestigious task of " +
                 "establishing a\nresearch outpost orbiting an alien planet a" +
                 " mechanical failure\nrendered you unable to reach a stable " +
                 "orbit over the planet. You\nhad no choice but to enter the " +
                 "planet's rich atmosphere and\ncrash-landed on one of its " +
                 "landmasses. Hunt, Work with friendly\nnatives, " +
                 "Brave the planet's hazards - but by all means...\nSurvive." +
                 "\n\nType help and click submit to see the list of commands.")


def load_game():
    global load_save
    
    f10.pack()
    title.pack_forget()
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()

    load_save = True
    print_prompt("Game loaded.")


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

# # #END Page Switches# # #


# # #Frames# # #
f1 = Frame(root, bg='#3b444b')
f2 = Frame(root, bg='#3b444b')
f3 = Frame(root, bg='#3b444b')
f4 = Frame(root, bg='#3b444b')
f5 = Frame(root, bg='#3b444b')
f6 = Frame(root, bg='#3b444b')
f7 = Frame(root, bg='#3b444b')
# # #END Frames# # #

title = Label(root, text="Crashed", font=("Courier", 54), pady=70, fg='white',
              bg='#3b444b')
title.pack() 

# # #Main Page# # #
frame0 = Frame(f1, bg='#3b444b', pady=5)
frame1 = Frame(f1)
frame2 = Frame(f1, bg='#3b444b', pady=5)

button = Button(frame0, text="Login", bg='#cc5500', fg='white', width=15,
                command=login_page)
button.pack(side=LEFT, anchor="nw")

button = Button(frame1, text="Signup", bg='#cc5500', fg='white', width=15,
                command=signup_page)
button.pack(side=LEFT, anchor="nw")

button = Button(frame2, text="Exit", bg='#FF0000', fg='white', width=15,
                command=root.destroy)
button.pack(side=LEFT, anchor="nw")

frame0.pack()
frame1.pack()
frame2.pack()
# # #END Main Page# # #


# # #Login Page# # #
# this clears out the text in the text box for username
def clear_username1(event):
    username2.delete(0, END)


def clear_password1(event):
    password2.delete(0, END)


frame1 = Frame(f2, bg='#3b444b', pady=10)
frame2 = Frame(f2)
frame3 = Frame(f2, bg='#3b444b', pady=10)

# username entry box is here
username2 = Entry(frame1, width=25)
username2.insert(0, "Username") 
username2.pack(side=LEFT, anchor="nw")
username2.bind("<Button-1>", clear_username1)
# # #LOGIN USERNAME END# # #

# password for the login part
password2 = Entry(frame2, width=25)
password2.insert(0, "Password")
password2.pack(side=LEFT, anchor="nw")
password2.bind("<Button-1>", clear_password1)
# # #Pasword END# # #

button = Button(frame3, text="Back", bg='#cc5500', fg='white', width=15,
                command=login_back)
button.pack(side=LEFT, anchor="nw")

button = Button(frame3, text="Login", bg='#cc5500', fg='white', width=15,
                command=start_game)
button.pack(side=LEFT, anchor="nw")

frame1.pack()
frame2.pack()
frame3.pack()
# # #END Login Page# # #


# # #Sign Up Page# # #
# this clears out the text in the text box for username
def clear_username2(event):
    username1.delete(0, END)


def clear_password2(event):
    password1.delete(0, END)


def clear_name1(event):
    name1.delete(0, END)


frame0 = Frame(f3, bg='#3b444b', pady=10)
frame1 = Frame(f3, bg='red')
frame2 = Frame(f3, bg='#3b444b', pady=10)
frame3 = Frame(f3, bg='yellow')

# name entry box is here
name1 = Entry(frame0, width=25)
name1.insert(0, "Name")
name1.pack(side=LEFT, anchor="nw")
name1.bind("<Button-1>", clear_name1)
# # #NAME END# # #

# username entry box is here
username1 = Entry(frame1, width=25)
username1.insert(0, "Username") 
username1.pack(side=LEFT, anchor="nw")
username1.bind("<Button-1>", clear_username2)
# # #LOGIN USERNAME END# # #

# password for the login part
password1 = Entry(frame2, width=25)
password1.insert(0, "Password")
password1.pack(side=LEFT, anchor="nw")
password1.bind("<Button-1>", clear_password2)
# # #Pasword END# # #

button = Button(frame3, text="Back", bg='#cc5500', fg='white', width=15,
                command=signup_back)
button.pack(side=LEFT, anchor="nw")

button = Button(frame3, text="Signup", bg='#cc5500', fg='white', width=15,
                command=start_game)
button.pack(side=LEFT, anchor="nw")

frame0.pack()
frame1.pack()
frame2.pack()
frame3.pack()
# # #End Sign Up Page# # #

# # #Menu# # #
frame0 = Frame(f4, bg='#3b444b', pady=5)
frame1 = Frame(f4, bg='red')
frame2 = Frame(f4, bg='#3b444b', pady=5)
frame3 = Frame(f4, bg='yellow')
frame4 = Frame(f4, bg='#3b444b', pady=5)
frame5 = Frame(f4, bg='yellow')

button = Button(frame0, text="New Game", bg='#cc5500', fg='white', width=15,
                command=new_game)
button.pack(side=LEFT, anchor="nw")

button = Button(frame1, text="Load Game", bg='#cc5500', fg='white', width=15,
                command=load_game)
button.pack(side=LEFT, anchor="nw")

button = Button(frame2, text="Info", bg='#cc5500', fg='white', width=15,
                command=info)
button.pack(side=LEFT, anchor="nw")

button = Button(frame3, text="Help", bg='#cc5500', fg='white', width=15,
                command=help5)
button.pack(side=LEFT, anchor="nw")

button = Button(frame4, text="Settings", bg='#cc5500', fg='white', width=15,
                command=settings)
button.pack(side=LEFT, anchor="nw")

button = Button(frame5, text="Log Out", bg="#FF0000", fg='white', width=15,
                command=back_menu)
button.pack(side=LEFT, anchor="nw")

frame0.pack()
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()
# # #END Menu# # #

# # #Info Tab# # #
c1 = Canvas(f5, bg='#5a6873', width=500, height=400)

# the info tab and the underline part
font1 = tkFont.Font(family="Courier", size=13, weight="bold")
c1.create_text(30, 20, text="Info:", font=font1, fill='white')

# info goes here
c1.create_text(250, 50,
               text="Disaster! Once assigned the prestigious task of establish"
                    "ing a research outpost orbiting", fill='white')
c1.create_text(250, 65,
               text="an alien planet to study the rudimentary life forms, a m"
                    "echanical failure rendered", fill='white')
c1.create_text(250, 80,
               text="you unable to reach a stable orbit over the planet. You h"
                    "ad no choice but to enter the", fill='white')
c1.create_text(250, 95,
               text="planet's rich atmosphere and crash landed on one of its "
                    "islands. Nonetheless, protocol", fill='white')
c1.create_text(250, 110,
               text="dictates that radio silence for a period of 5 rotations ("
                    "5 days) will necessitate a ", fill='white')
c1.create_text(250, 125,
               text="search-and-rescue mission to be dispatched. Hunt, Work wi"
                    "th friendly natives, Brave the", fill='white')
c1.create_text(250, 140,
               text="planet's hazards - but by all means... Survive.",
               fill='white')

# back button
button = Button(c1, text="Back", bg='#cc5500', fg='white', width=15,
                command=info_back)
button.pack()
c1.create_window(75, 375, window=button)

c1.pack()
# # #End Info Tab# # #

# # #Settings Tab# # #
c3 = Canvas(f6, bg='#5a6873', width=500, height=400)

# title for settings
font1 = tkFont.Font(family="Courier", size=13, weight="bold")
c3.create_text(50, 20, text="Settings:", font=font1, fill='white')

# settings options
font2 = tkFont.Font(family="Courier", size=10)

c3.create_text(200, 40, text="---", font=font2, fill='white')
set1 = Checkbutton(c3, bg='#5a6873')
c3.create_window(230, 40, window=set1)


# back button
button = Button(c3, text="Back", bg='#cc5500', fg='white', width=15,
                command=settings_back)
button.pack()
c3.create_window(75, 375, window=button)

# update button
button = Button(c3, text="Update", bg='#cc5500', fg='white', width=15)
button.pack()
c3.create_window(425, 375, window=button)

c3.pack()

# # #End Settings Tab# # #

# # #Help Tab# # #
c2 = Canvas(f7, bg='#5a6873', width=500, height=400)

# the info tab and the underline part
font1 = tkFont.Font(family="Courier", size=13, weight="bold")
c2.create_text(30, 20, text="Help:", font=font1, fill='white')

# title and box
font2 = tkFont.Font(family="Courier", size=10)
c2.create_text(90, 50, text="Title:", font=font2, fill='white')

box1 = Entry(c2, width=50)
box1.pack()

c2.create_window(275, 50, window=box1)
# descrip and box
c2.create_text(65, 75, text="Description:", font=font2, fill='white')

box2 = Entry(c2, width=50)
box2.pack()

c2.create_window(275, 75, window=box2)


# back button
button = Button(c2, text="Back", bg='#cc5500', fg='white', width=15,
                command=help_back)
button.pack()
c2.create_window(75, 375, window=button)

# submit button
button = Button(c2, text="Submit", bg='#cc5500', fg='white', width=15)
button.pack()
c2.create_window(425, 375, window=button)

c2.pack()

# # #End Help Tab# # #


# # #GAME INTERFACE# # #
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func    


# Actual transition from game UI to the main menu
def return_to_menu():
    midright.destroy()
    newMiniMap()
    # botright.destroy()
    newInventory()
    timer.refresh_label()
    userhealth.refresh_health()
    
    f10.pack_forget()
    title.pack()
    start_game()


# Called when 'Return to Menu' button is pushed ie game is over
def game_over():
    new_variables()
    menu_button.destroy()
    # new button for submit
    textbox_button = Button(textbox, text="Submit", bg='#cc5500', fg='white',
                            height=2, width=15, command=searchDirection)
    textbox_button.pack()
    textbox.create_window(496, 23, window=textbox_button)  # pack the box
    return_to_menu()


# changes the color of the score
def healthcolor():
    score = healthScore()
    if score >= 90:
        return "Green"
    elif 90 > score >= 40:
        return "Black"
    else:
        return "Red"


# this will be where the score is obtained
def healthScore():
    return player.get_health()


# this will be where it figures out what the text says
def searchDirection(event):
    result = entry10.get()
    player.get_user_input(cur_level, result)
    entry10.delete(0, END)

    midright.destroy()
    newMiniMap()
    # botright.destroy()
    newInventory()
    timer.refresh_label()
    userhealth.refresh_health()

    if player.is_game_over():
        print_prompt("You have died!")
        textbox_button.destroy()
        entry10.destroy()
        # new button for submit
        menu_button = Button(textbox, text="Back to Menu", bg='#cc5500',
                             fg='white', height=2, width=15, command=game_over)
        menu_button.pack()
        textbox.create_window(496, 23, window=menu_button)  # pack the box
    
    if player.get_location().get_next_level():
        prompt_move_nxt_level()


# this refreshes the mini map in the corner
def newMiniMap():
    midright = Canvas(canvas1, bg="#bbbbbb", width=290, height=290,
                      highlightthickness=3, highlightbackground="black")
    start_mini_map_IO(midright, player.get_location())

    midright.pack()
    canvas1.create_window(730, 230, window=midright)


# this refreshes the inventory in GUI
def newInventory():
    botright = Canvas(canvas1, bg="#bbbbbb", width=290, height=295,
                      highlightthickness=3, highlightbackground="black")
    inventory = Text(botright, height=18, width=37, bg="#bbbbbb",
                     highlightthickness=3, highlightbackground="black")
    inventory.config(state=NORMAL)
    
    # get all the inventory items
    items = {}
    for item in player.get_inventory():
        item_name = item.get_name()
        if item.get_type() == 'CONSUMABLE':
            items[item_name] = item.get_use_count()
        else:
            if item_name in items.keys():
                items[item_name] += 1
            else:
                items[item_name] = 1
    # print the inventory
    for key in items:
        inventory.insert(END, key + ': ' + str(items[key]) + '\n')
    inventory.insert(END, '\n\n(Enter "inventory" for inventory description)')
    
    inventory.config(state=DISABLED)
    botright.pack()
    inventory.pack()
    canvas1.create_window(733, 533, window=botright)


# Directly prints a prompt to the dialog box to the left
def print_prompt(value):
    dialogleft = Canvas(canvas1, bg="#bbbbbb", width=550, height=600,
                        highlightthickness=3, highlightbackground="black")
    prompt = Text(dialogleft, height=35, width=65, bg="#bbbbbb",
                  highlightthickness=0)
    prompt.config(state=NORMAL)
    prompt.insert(END, value)
    prompt.config(state=DISABLED)
    dialogleft.pack()
    prompt.pack()
    canvas1.create_window(300, 325, window=dialogleft)


def identify_start_room(level):
    # returns room with greatest distance from nxt_lvl event ie start_room
    for room in level:
        if room.get_next_level():
            nxt_lvl_room = room
            break
    nxt_lvl_position = nxt_lvl_room.get_position()
    
    # use below as standard in case there is only 1 room in level.
    # otherwise it is bound to change
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


# handles the transition between levels
def transition_new_level():
    global cur_level, level_idx, player
    
    if level_idx+1 < len(levels):
        new_level = levels[level_idx+1]
    else:  # if all levels are complete
        new_level = None
    
    if new_level is None:  # all levels complete
        print_prompt(level_transitions[-1])
        textbox_button.destroy()
        entry10.destroy()
        # new button for submit
        menu_button = Button(textbox, text="Back to Menu", bg='#cc5500',
                             fg='white', height=2, width=15, command=game_over)
        menu_button.pack()
        textbox.create_window(496, 23, window=menu_button)  # pack the box
    elif new_level != cur_level:
        level_idx += 1
        cur_level = new_level
        player.set_start_position(identify_start_room(cur_level))
        print_prompt(level_transitions[level_idx - 1])


# prompt user whether they want to move to the next level
def prompt_move_nxt_level():
    # Returns either True/False
    response = Tk(className=" Progression")
    response.config(bg='#3b444b')
    title = Label(response, text='Advance to the next level?', pady=30,
                  font=("Courier", 12), fg='white', bg='#3b444b')
    Yes = Button(response, text="Yes", padx=30, pady=5,
                 command=combine_funcs(transition_new_level, response.destroy,
                                       midright.destroy, newMiniMap),
                 bg='#cc5500', fg='white', highlightthickness=0)
    No = Button(response, text="No", padx=30, pady=5, command=response.destroy,
                bg='#cc5500', fg='white', highlightthickness=0)
    title.grid(row=0, columnspan=2)
    Yes.grid(row=1, column=0)
    No.grid(row=1, column=1)


# creates new objects for all the game variables
def new_variables():
    global levels, player, cur_level, level_idx
    # create new game
    levels = [
        gen_random_level(level_size[0], 1),
        gen_random_level(level_size[1], 2),
        gen_random_level(level_size[2], 3),
        gen_random_level(level_size[3], 4),
        gen_random_level(level_size[4], 5),
    ]
    level_idx = 0
    cur_level = levels[level_idx]
    player = Player(canvas1)
    player.set_start_position(identify_start_room(cur_level))
    
# GAME SETTINGS


# # #Frames# # #
f10 = Frame(root, bg='#3b444b')
# # #End Frames
canvas1 = Canvas(f10, bg='#3b444b', width=900, height=700, highlightthickness=0)

# Game Variables
level_size = [10, 12, 15, 18, 23]
levels = [
    gen_random_level(level_size[0], 1),
    gen_random_level(level_size[1], 2),
    gen_random_level(level_size[2], 3),
    gen_random_level(level_size[3], 4),
    gen_random_level(level_size[4], 5),
]
level_idx = 0
cur_level = levels[level_idx]
player = Player(canvas1)
player.set_start_position(identify_start_room(cur_level))

if load_save:
    # TODO: add the load game method here
    # 1. Download game data from database
    # 2. Set it to the game variables level_idx, cur_level, and player
    next

# font for texts on screen
font2 = tkFont.Font(family="Courier", size=13, weight="bold")

# dialog box on the left
dialogleft = Canvas(canvas1, bg="#bbbbbb", width=550, height=600,
                    highlightthickness=3, highlightbackground="black")
dialogleft.pack()
canvas1.create_window(300, 325, window=dialogleft)

# the box you can type on on the bottom right
textbox = Canvas(canvas1, bg="white", width=550, height=40,
                 highlightthickness=3, highlightbackground="black")

textbox.create_text(15, 23, text=">", font=font2, fill="black")
entry10 = Entry(textbox, width=65)  # this is the entry box
entry10.bind("<Return>", searchDirection)
entry10.pack()
textbox.create_window(230, 23, window=entry10)  # packing the entry box

# new button for submit
textbox_button = Button(textbox, text="Submit", bg='#cc5500', fg='white',
                        height=2, width=15, command=searchDirection)
textbox_button.pack()
textbox.create_window(496, 23, window=textbox_button)  # pack the box

# Used to return to the menu
# new button for submit
menu_button = Button(textbox, text="Back to Menu", bg='#cc5500', fg='white',
                     height=2, width=15, command=game_over)

textbox.pack()
canvas1.create_window(300, 660, window=textbox)

# top right health and day box
topright = Canvas(canvas1, bg="#bbbbbb", width=290, height=50,
                  highlightthickness=3, highlightbackground="black")


class Timer:
    def __init__(self, parent, player):
        # label displaying time
        self.label = Label(parent, text=player.get_time(),
                           font="Courier 13 bold", width=14)
        self.label.pack()

    def refresh_label(self):
        """ refresh the content of the label every second """
        finalText = "%s" % (player.get_time())
        self.label.configure(text=finalText)


class Health:
    def __init__(self, parent):
        self.health = 100
        self.label = Label(parent, text="Health %d/100" % (healthScore()),
                           font="Courier 13 bold", width=15, fg=healthcolor())
        self.label.pack()

    def refresh_health(self):
        finalText = "Health %d/100" % (healthScore())
        self.label.configure(text=finalText, fg=healthcolor())


healthscore = Canvas(topright, bg="#bbbbbb", width=100, height=50)
userhealth = Health(healthscore)

usertime = Canvas(topright, bg="#bbbbbb", width=100, height=50)
timer = Timer(usertime, player)

healthscore.pack(side="left")
usertime.pack(side="right")

topright.pack()
canvas1.create_window(730, 50, window=topright)

# map box middle right
midright = Canvas(canvas1, bg="#bbbbbb", width=290, height=290,
                  highlightthickness=3, highlightbackground="black")

start_mini_map_IO(midright, player.get_location())

midright.pack()
canvas1.create_window(730, 230, window=midright)

# inventory box bottom right
newInventory()


canvas1.pack()


# f10.pack()


# # #END GAME INTERFACE# # #

f1.pack()
f6.pack_forget()
root.mainloop()
