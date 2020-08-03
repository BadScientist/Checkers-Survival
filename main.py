import random
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

level_1 = gen_random_level(10, 1)
level_2 = gen_random_level(10, 2)
level_3 = gen_random_level(10, 3)
level_4 = gen_random_level(10, 4)
level_5 = gen_random_level(10, 5)
cur_level = level_1
player = Player(cur_level[0])


def main():
    print("Crashed")
    # while not test_player.is_game_over():
    #     test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()
