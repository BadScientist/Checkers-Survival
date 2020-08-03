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

# TODO: ensure user doesn't spawn in room with 'next-level' event

level_idx = 0
level_size = [10, 15, 20, 25, 30]
levels = [
    gen_random_level(level_size[0], 1),
    gen_random_level(level_size[1], 2),
    gen_random_level(level_size[2], 3),
    gen_random_level(level_size[3], 4),
    gen_random_level(level_size[4], 5),
]

#repeat following commands for each level (once user progresses to new lvl)
cur_level = levels[level_idx]
start_room = cur_level[randint( 0, level_size[level_idx]-1 )]
while start_room.get_next_level() == True:
    start_room = cur_level[randint( 0, level_size[level_idx]-1 )]

player = Player(start_room)

print('here')


def main():
    print("Crashed")
    # while not test_player.is_game_over():
    #     test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()