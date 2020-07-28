from item import *
from room import *
from player import *
from copy import deepcopy
import mapGUI
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os

#Import the Main Menu from interface like a Macro
from interface import *


def main():    
    random.seed()
    level_1 = gen_random_level(10)
    meat = Consumable("MEAT", "A hunk of meat. Eat it to gain health.", 10, 1)
    mp = Consumable("MEDPACK", "A first aid kit that will fully restore your health.", 100, 1)
    hk = Weapon("KNIFE", "A plain hunting knife.", 10, 15)
    hunter = create_character("HUNTER",
                              "You see a <n> leaning against a nearby tree.",
                              "\"Hello there. If you have a <iw>, I'll trade you this <io> for it.\"",
                              mp, meat)
    bunny = create_animal("BUNNY",
                   "There is a small space <n> hopping about nearby.",
                   16, 0.5, 5, meat)
    level_1[0].character = hunter
    level_1[0].animal = bunny
    test_player = Player("Johnnie", level_1[0])
    test_player.add_item(deepcopy(mp))
    test_player.add_item(deepcopy(hk))
    while True:

        # To test the mini map remove these comments:

        # root = tk.Tk(className=" Example Gameplay")
        # root.config(bg='#3b444b')
        # root.geometry("880x660")
        # mapGUI.start_mini_map_IO(root, level_1[0])
        # root.mainloop()

        # Then close it to continue with rest of main()

        test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()