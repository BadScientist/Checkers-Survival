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
import os, math

# Import the Main Menu from interface like a Macro
from interface import *

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

player = Player()
player.set_start_position(identify_start_room(cur_level))

print_prompt('HAHSHCJSBCJBASJK')

def main():
    print("Crashed")
    # while not test_player.is_game_over():
    #     test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()
