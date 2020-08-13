from random import randrange
from tkinter import *


def event_to_UI(title_txt):
    # param title_txt: the prompt
    event_UI = Tk(className=" Event")
    event_UI.config(bg='#3b444b')
    title = Label(event_UI, text=title_txt, pady=30, font=("Courier", 12),
                  fg='white', bg='#3b444b')
    adj = IntVar(event_UI, name="adj")
    
    choice_1 = Button(event_UI, text="1", padx=30, pady=5,
                      command=lambda: event_UI.setvar(name="adj", value=1),
                      bg='#cc5500', fg='white', highlightthickness=0)
    choice_2 = Button(event_UI, text="2", padx=30, pady=5,
                      command=lambda: event_UI.setvar(name="adj", value=2),
                      bg='#cc5500', fg='white', highlightthickness=0)
    choice_3 = Button(event_UI, text="3", padx=30, pady=5,
                      command=lambda: event_UI.setvar(name="adj", value=3),
                      bg='#cc5500', fg='white', highlightthickness=0)
    title.grid(row=0, columnspan=3)
    choice_1.grid(row=1, column=0)
    choice_2.grid(row=1, column=1)
    choice_3.grid(row=1, column=2)
    event_UI.wait_variable(adj)
    event_UI.destroy()
    return adj.get()


def result_to_UI(title_txt):
    # param title_txt: the prompt
    event_UI = Tk(className=" Event Result")
    event_UI.config(bg='#3b444b')
    title = Label(event_UI, text=title_txt, pady=30, font=("Courier", 12),
                  fg='white', bg='#3b444b')
    ok = Button(event_UI, text="OK", padx=30, pady=5, command=event_UI.destroy, 
                bg='#cc5500', fg='white', highlightthickness=0)
    title.pack()
    ok.pack()


def cave_in():
    adj_values = [0, 10, 0]
    choice = event_to_UI('The ground begins to shake beneath your feet. '
                         'Thinking quickly, you...\n\n1 - dive forward.\n' +
                         '2 - stand still.\n3 - roll backwards.')
    if choice == 2:
        result_to_UI("The ground caves in beneath your feet and you " +
                     "fall into a sinkhole!\n You were injured by the fall.")
    else:
        result_to_UI("You move out of the way just before the ground " +
                     "caves in!\nYou continue on your way without injury.")
    return adj_values[choice - 1]


def creature_attack():
    adj_values = [20, 20, 0]
    choice = event_to_UI('You hear a slight crunch behind you. You...\n\n' +
                         '1 - turn around slowly.\n2 - keep walking.\n' +
                         '3 - quickly pull out you weapon and turn around.')
    if choice == 3:
        result_to_UI("A huge jabbin tries to lunge at you, but you " +
                     "strike it just in time!\nThe injured creature runs " +
                     "away.\nYou continue on your way without injury.")
    else:
        result_to_UI("You are pounced on by a huge jabbin!\nYou manage to " +
                     "fight it off, but not before it injures you.")
    return adj_values[choice - 1]


def poison_cloud():
    adj_values = [10, 0, 20]
    choice = event_to_UI('You smell something strange. It keeps getting ' +
                         'stronger as you walk. You...\n\n1 - cover your ' +
                         'nose and mouth with your hand.\n2 - move to higher' +
                         ' ground.\n3 - hold your breath.')
    if choice == 1:
        result_to_UI("Noxious gas leaks through your fingers, poisoning you!")
    elif choice == 2:
        result_to_UI("You manage to make it to a hilltop just before a " +
                     "noxious cloud fills the low ground around you!" +
                     "\nOnce the cloud dissipates, you continue on " +
                     "without injury.")
    else:
        result_to_UI("You hold your breath as long as you can, but " +
                     "eventually you have to breath.\nYou inhale a large " +
                     "amount of noxious gas!")
    return adj_values[choice - 1]


def flood():
    adj_values = [15, 15, 0]
    choice = event_to_UI('You hear a rumbling noise in the distance. The ' +
                         'sound keeps getting louder and louder. You...\n\n' +
                         '1 - turn toward the sound and wait.\n2 - dive ' +
                         'forward.\n3 - move to higher ground.')
    if choice == 1:
        result_to_UI("A flash flood rushes in and knocks you off your feet!\n" +
                     "You are battered by debris, but manage not to drown by" +
                     " clinging to the flotsam.")
    elif choice == 2:
        result_to_UI("You try to dive out of the way, but it does you no " +
                     "good as a flash flood rushes over you!\nYou are " +
                     "battered by debris, but manage not to drown by " +
                     "clinging to the flotsam.")
    else:
        result_to_UI("You manage to make it to a hilltop just before a flash" +
                     " flood fills the low ground around you!\nOnce the " +
                     "water recedes, you continue on without injury.")
    return adj_values[choice - 1]


def storm():
    adj_values = [0, 20, 10]
    choice = event_to_UI('Clouds begin to gather in the sky above you. As ' +
                         'it gets darker and darker, you decide to...\n\n1 ' +
                         '- find shelter.\n2 - move to higher ground.\n3 - ' +
                         'keep moving.')
    if choice == 1:
        result_to_UI("You manage to find shelter in a shallow cave just " +
                     "before a massive storm hits.\nYou wait for the storm " +
                     "to pass before moving on unharmed.")
    elif choice == 2:
        result_to_UI("You make it to a hilltop just as a massive storm hits." +
                     "\nBeing so high up only puts you in more danger as " +
                     "lightning strikes right next to you!\nYou aren't hit " +
                     "directly, but you are still injured by the blast.")
    else:
        result_to_UI("As you continue on, a massive storm hits!\nThe powerful" +
                     "winds batter you with debris, injuring you.")
    return adj_values[choice - 1]


event_master_list = [cave_in, creature_attack, poison_cloud, flood, storm]


def gen_event():
    """
    Returns None or a random event function based on the given level_num number.
    """
    # 20% chance of returning character instead of None
    if randrange(0, 5) == 4:
        return event_master_list[randrange(0, len(event_master_list))]

    else:
        return None
