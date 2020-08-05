from random import *
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
start_room = cur_level[randint( 0, level_size[level_idx]-1 )]
while start_room.get_next_level():
    start_room = cur_level[randint( 0, level_size[level_idx]-1 )]

player = Player()
player.set_start_position(start_room)


def main():
    print("Crashed")
    # while not test_player.is_game_over():
    #     test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()
