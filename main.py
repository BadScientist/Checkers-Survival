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

def next_level(curr_level_idx, player):
    #returns the next level
    curr_level_idx += 1
    if curr_level_idx < len(levels):
        new_level = levels[curr_level_idx]
        start_room = new_level[randint( 0, level_size[curr_level_idx]-1 )]
        while start_room.get_next_level() == True:
            start_room = new_level[randint( 0, level_size[curr_level_idx]-1 )]
        player.set_start_position(start_room)
        return new_level
    else: #if all levels are complete
        return None

level_size = [10, 12, 15, 18, 23]
levels = [
    gen_random_level(level_size[0], 1),
    gen_random_level(level_size[1], 2),
    gen_random_level(level_size[2], 3),
    gen_random_level(level_size[3], 4),
    gen_random_level(level_size[4], 5),
]

#Initialize first Level and Player
level_idx = 0
cur_level = levels[level_idx]
start_room = cur_level[randint( 0, level_size[level_idx]-1 )]
while start_room.get_next_level() == True:
    start_room = cur_level[randint( 0, level_size[level_idx]-1 )]

player = Player(start_room)

def main():
    print("Crashed")
    # while not test_player.is_game_over():
    #     test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()