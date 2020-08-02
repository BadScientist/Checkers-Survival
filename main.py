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

    while not test_player.is_game_over():
        test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()
