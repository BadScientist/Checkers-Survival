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

# Import the Main Menu from interface like a Macro
from interface import *


def main():    
    random.seed()
    level_3 = gen_random_level(10, 3)
    test_player = Player("Johnnie", level_3[0])

    while True:

        # To test the mini map remove these comments:

        # root = tk.Tk(className=" Example Gameplay")
        # root.config(bg='#3b444b')
        # root.geometry("880x660")
        # mapGUI.start_mini_map_IO(root, level_1[0])
        # root.mainloop()

        # Then close it to continue with rest of main()

        test_player.get_user_input(level_3)


if __name__ == "__main__":
    main()