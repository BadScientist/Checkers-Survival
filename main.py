from item import *
from room import *
from player import *
import mapGUI
from tkinter import *
# from PIL import ImageTk, Image
import tkinter.font as tkFont
# from PIL import Image, ImageTk
import os

#Import the Main Menu from interface like a Macro
from interface import *

def main():    
    random.seed()
    level_1 = gen_random_level(10)
    hunting_knife = Weapon("Hunting Knife",
                           "A plain hunting knife.",
                           10, 15)
    health_pack = Consumable("Health Pack",
                             "A simple health pack.",
                             30, 1)
    test_player = Player("Johnnie", level_1[0])
    test_player.add_item(hunting_knife)
    test_player.add_item(health_pack)
    while True:
        #       To test the mini map remove these comments:
        #
        #root = tk.Tk(className=" Example Gameplay")
        #root.config(bg='#3b444b')
        #root.geometry("880x660")
        #mapGUI.start_mini_map_IO(root, level_1[0])
        #root.mainloop()
        #
        #Then close it to continue with rest of main()
    
        test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()