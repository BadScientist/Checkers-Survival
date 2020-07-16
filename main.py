import random
from room import *

# example use of functions below class definition
class item:
    """Item class of the game."""
    def __init__(self, name, str_desc):
        """Creates an  item object.\n
        parameters: name, str_desc"""
        self._name = name
        self._str_desc = str_desc
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def description(self):
        """Returns a string description of the item."""
        return self._str_desc
    
    def set_description(self, desc):
        """Sets description of the item."""
        self._str_desc = desc

    def __str__(self):
        return self._name + ": " + self._str_desc


class weapon(item):
    """Weapon class of the game."""
    def __init__(self, name, str_desc, dmg_low, dmg_high):
        """Creates a weapon object.\n
        parameters: name, str_desc, dmg_low, dmg_high"""
        self._name = name
        self._str_desc = str_desc
        self._dmg_low = dmg_low
        self._dmg_high = dmg_high
    
    def __str__(self):
        return self._name + ": " + self._str_desc + " Min Damage: " + str(self._dmg_low) + ", Max Damage:" + str(self._dmg_high) 
    
    def rand_dmg(self):
        """Returns randomized dmg value between dmg low and dmg_high (inclusive)."""
        return random.randrange(self._dmg_low, self._dmg_high + 1)

    def get_low(self):
        """Returns low range of damage."""
        return self._dmg_low
    
    def get_high(self):
        """Returns high range of damage."""
        return self._dmg_high

class consumable(item):
    """Consumable class in game."""
    def __init__(self, name, str_desc, value, use_count):
        """Creates a consumable object.\n
        parameters: name, str_desc, value, use_count"""
        self._name = name
        self._str_desc = str_desc
        self._value = value
        self._use_count = use_count

    def __str__(self):
        return self._name + ": " + self._str_desc + " value: " + str(self._value) + ", use count:" + str(self._use_count) 
        
    def get_value(self):
        """get the value of the cosumable."""
        return self._value
    
    def get_use_count(self):
        """get the remaining use count"""
        return self._use_count

    #EDIT: this method should probably pass in a unit argument to change it
    # def use_item(self, unit):
    def use_item(self):
        """uses the item, decrementing the use count"""
        self._use_count -= 1
    
    def usable(self):
        """checks if item is usable"""
        return self._use_count > 0
    
    
class Player:
    def __init__(self, name, start_room, weapon):
        self._name = name
        self._health = 100
        self.location = start_room
        self._weapon = weapon
        self._inventory = [weapon]

    def move(self, dir_str):
        """
        Updates the player's location to the adjacent room in the given
        direction (if present) and displays the long_desc of the new room.
        """
        # Get the room in the given direction
        if dir_str == 'n' or dir_str == "north":
            adj_room = self.location.get_adjacent_room('N')

        elif dir_str == 's' or dir_str == "south":
            adj_room = self.location.get_adjacent_room('S')

        elif dir_str == 'e' or dir_str == "east":
            adj_room = self.location.get_adjacent_room('E')

        elif dir_str == 'w' or dir_str == "west":
            adj_room = self.location.get_adjacent_room('W')

        # Invalid entry error message
        else:
            print("You didn't enter a valid direction.")
            return

        # No adjacent room error message
        if adj_room is None:
            print("You can't go that way.")
            return
        else:
            self.location = adj_room
            self.here()

    def here(self):
        """
        Displays the long_desc of the Room that is currently set as the Player's
        location.
         """
        print(self.location.get_long_desc())

    def look(self, dir_str):

        # Get the room in the given direction
        if dir_str == 'n' or dir_str == "north":
            adj_room = self.location.get_adjacent_room('N')

        elif dir_str == 's' or dir_str == "south":
            adj_room = self.location.get_adjacent_room('S')

        elif dir_str == 'e' or dir_str == "east":
            adj_room = self.location.get_adjacent_room('E')

        elif dir_str == 'w' or dir_str == "west":
            adj_room = self.location.get_adjacent_room('W')

        # Invalid entry error message
        else:
            print("You didn't enter a valid direction.")
            return

        # No adjacent room error message
        if adj_room is None:
            print("There is nothing in that direction.")
            return
        else:
            print("To the " + dir_str + " you see " + adj_room.get_shrt_desc())

    def take(self, item_str):
        print("Took " + item_str)

    def use(self, item_str, target_str=None):
        if target_str is None:
            print("Used " + item_str)
        else:
            print("Used " + item_str + " on " + target_str)

    def hunt(self, target_str, weap_str):
        print("Hunted " + target_str + " with " + weap_str)

    def talk(self, npc_str):
        print("Talked to " + npc_str)

    def trade(self, npc_str):
        print("Traded your item for " + npc_str + "'s other item.")

    def display_inventory(self):
        if len(self._inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for item in self._inventory:
                print(item)

    def display_map(self):
        print("You look at your map.")

    def display_status(self):
        print("Health: " + str(self._health) + "/100")

    # set functions
    def adj_health(self, amount):
        """Adjusts the player's health by the given amount."""
        self._health += amount

    def add_item(self, item):
        self._inventory.append(item)

    def set_weapon(self, weapon):
        self._weapon = weapon

    # get functions
    def get_health(self):
        return self._health

    def get_weapon(self):
        return self._weapon

    def get_item(self, item_num):
        return self._inventory[item_num]

    def get_user_input(self):

        # Get input. Prompt is placeholder.
        curr_input = input("What do you want to do?: ")
        words = []
        curr_word = ""
    
        for letter in curr_input.lower():
    
            # Concat non-space characters into words
            if letter != ' ':
                curr_word += letter
    
            # Add words separated by spaces to words list
            else:
                words.append(curr_word)
                curr_word = ""
    
        words.append(curr_word)  # Add final word to list
    
        # Call methods based on user input.
        if words[0] == "move":
            if len(words) == 1:
                print("You must specify a valid direction to move.")
            else:
                self.move(words[1])  # To be updated based on player class
    
        elif words[0] == "look":
            if len(words) == 1:
                print("You must specify a valid direction to look.")
            else:
                self.look(words[1])  # To be updated based on player class
    
        elif words[0] == "take":
            if len(words) == 1:
                print("You must specify a valid item to take.")
            else:
                self.take(words[1])  # To be updated based on player class
    
        elif words[0] == "use":
    
            if len(words) == 1:
                print("You must specify a valid item to use.")
    
            # Use item.
            elif len(words) == 2:
                self.use(words[1])  # To be updated based on player class
    
            # Use item on target.
            else:
                self.use(words[1], words[2])  # To be updated based on player class
    
        elif words[0] == "hunt":
    
            if len(words) < 3:
                print("You must specify a target and a weapon to use.")
    
            # Hunt target with weapon.
            else:
                self.hunt(words[1], words[2])  # To be updated based on player class
    
        elif words[0] == "talk":
    
            if len(words) < 2:
                print("You must specify who you want to talk to.")
    
            else:
                self.talk(words[1])  # To be updated based on player class
    
        elif words[0] == "trade":
    
            if len(words) < 2:
                print("You must specify who you with to trade with.")
    
            else:
                self.trade(words[1])
    
        elif words[0] == "inventory":
            self.display_inventory()  # To be updated based on player class
    
        elif words[0] == "map":
            self.display_map()  # To be updated based on player class
    
        elif words[0] == "status":
            self.display_status()  # To be updated based on player class
    
        elif words[0] == "here":
            self.here()  # To be updated based on player class
    
        # Display help information about commands
        elif words[0] == "help":
    
            # Display command list
            if len(words) == 1:
                print("Commands: move, look, take, use, hunt, talk, trade, inventory, map, status, here, help")
    
            elif words[1] == "move":
                print("Usage: move <direction>")
                print("Move to the location in the specified direction.")
    
            elif words[1] == "look":
                print("Usage: look <direction>")
                print("Look in the specified direction.")
    
            elif words[1] == "take":
                print("Usage: take <item>")
                print("Take the specified item.")
    
            elif words[1] == "use":
                print("Usage: use <item> OR use <item> <target>")
                print("Use the specified item. Optionally use item on specified target.")
    
            elif words[1] == "hunt":
                print("Usage: hunt <weapon> <animal>")
                print("Hunt the specified animal with the specified weapon.")
    
            elif words[1] == "talk":
                print("Usage: talk <NPC name>")
                print("Talk to the specified NPC.")
    
            elif words[1] == "trade":
                print("Usage: trade <NPC name>")
                print("Trade with the specified NPC.")
    
            elif words[1] == "inventory":
                print("Usage: inventory")
                print("Display the items in the player's inventory.")
    
            elif words[1] == "map":
                print("Usage: map")
                print("Display the rooms the player has visited.")
    
            elif words[1] == "status":
                print("Usage: status")
                print("Display the player's status.")
    
            elif words[1] == "here":
                print("Usage: here")
                print("Display the description of current location.")
    
            elif words[1] == "help":
                print("Usage: help OR help <command>")
                print("Display command help information.")
    
            else:
                print("Commands: move, look, take, use, hunt, talk, trade, inventory, map, status, here, help")
    
        else:
            print("You didn't enter a valid command. Type \"help\" for a list of commands.")

        print("**************************************************")


random.seed()


def main():
    level_1 = gen_random_level(10)
    knife = weapon("Knife", "Used for hunting.", 2, 6)
    test_player = Player("Johnnie", level_1[0], knife)
    while True:
        test_player.get_user_input()


if __name__ == "__main__":
    main()
