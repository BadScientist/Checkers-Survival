import random
import copy
from room import *
from item import *
from NPCs import *


# example use of functions below class definition
class Player:
    def __init__(self, name, start_room):
        self._name = name
        self._health = 100
        start_room.apply_seen() #To view adjacent room contents in Maps
        self.location = start_room
        self._weapon = None
        self._inventory = []

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
            adj_room.apply_seen() #To view adjacent room contents in Maps
            self.location = adj_room
            self.here()

    def here(self):
        """
        Displays the long_desc of the Room that is currently set as the Player's
        location.
         """
        print(self.location.get_long_desc())
        if self.location.get_character() is not None:
            print(self.location.get_character().get_description())

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
            adj_room.apply_seen() #To view adjacent room contents in Maps
            print("To the " + dir_str + " you see " + adj_room.get_shrt_desc())

    def take(self, item_str):
        print("Took " + item_str)

    def use(self, item_str, target_str=None):
        if target_str is None:
            print("Used " + item_str)
        else:
            print("Used " + item_str + " on " + target_str)

    def hunt(self, target_str):
        if self._weapon is None:
            print("You must equip a weapon to hunt.")
            return
        print("Hunted " + target_str)

    def talk(self):
        """
        Talk to the Character in the Room in which the Player is located.
        """

        if self.location.get_character() is not None:
            print(self.location.get_character().get_dialogue())

        else:
            print("There is no one here to talk to.")

    def trade(self):
        """
        Trade with the Character in the Room in which the Player is located.
        """
        character = self.location.get_character()
        item_wanted = character.get_item_wanted()
        item_offered = character.get_item_offered()

        if character is not None:
            if not character.is_trade_complete():

                # Check if the player has the item_wanted.
                for item1 in self._inventory:
                    if item1.get_name() == item_wanted.get_name():

                        # Check if Player already has the same item as offered.
                        # If so, add use_count of the item in inventory to the
                        # item offered and remove the item from the inventory
                        # before adding the new item to the inventory.
                        for item2 in self._inventory:
                            if item2.get_name() == item_offered.get_name():
                                item_offered.adj_use_count(item2.get_use_count())
                                self._inventory.remove(item2)
                        self._inventory.append(item_offered)

                        # Remove 1 count of the traded item from the inventory.
                        # If no more uses, remove the item from the inventory.
                        item1.adj_use_count(-1)
                        if item1.get_use_count() < 1:
                            self._inventory.remove(item1)

                        character.set_trade_complete()
                        print("\"Thanks for the trade.\"")
                        return

                print("You don't have the correct item to trade.")

            else:
                print("\"Sorry, I have nothing left to trade.\"")

        else:
            print("There is no one here to trade with.")

    def display_inventory(self):
        print("Equipped Weapon:\n-", self._weapon, "\n\nInventory:")
        if len(self._inventory) == 0:
            print("Your inventory is empty.")
        else:
            for item in self._inventory:
                print("-",item)

    def display_map(self, level):
        start_large_map_IO(level, self.location)
        print("You look at your map.")

    def display_status(self):
        print("Health: " + str(self._health) + "/100")

    # set functions
    def adj_health(self, amount):
        """Adjusts the player's health by the given amount."""
        self._health += amount

    def add_item(self, item):
        self._inventory.append(item)

    def equip(self, weapon_str):
        """
        Exchange the equipped weapon for the specified weapon in the inventory.
        :param weapon_str: user input string from get_player_input
        :return:
        """
        weapon = None

        # Search for specified weapon in inventory.
        for item in self._inventory:
            if item.get_name() == weapon_str:

                # Check that the item is a weapon.
                if item.get_type() != "WEAPON":
                    print("You can't equip that.")
                    return

                weapon = item
                self._inventory.remove(item)
                break

        # If present, exchange inventory weapon for equipped weapon.
        if weapon is not None:
            if self._weapon is not None:
                self._inventory.append(self._weapon)
            self._weapon = weapon
            self.display_inventory()

        else:
            print("You don't have a " + weapon_str + " in your inventory.")

    # get functions
    def get_health(self):
        return self._health

    def get_weapon(self):
        return self._weapon

    def get_item(self, item_num):
        return self._inventory[item_num]

    def get_user_input(self, level):

        # Get input. Prompt is placeholder.
        curr_input = input("What do you want to do?: \n >")
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
                self.use(words[1],
                         words[2])  # To be updated based on player class

        elif words[0] == "hunt":

            if len(words) < 2:
                print("You must specify a target.")

            # Hunt target with weapon.
            else:
                self.hunt(words[1])  # To be updated based on player class

        elif words[0] == "talk":
            self.talk()  # To be updated based on player class

        elif words[0] == "trade":
            self.trade()

        elif words[0] == "inventory":
            self.display_inventory()  # To be updated based on player class

        elif words[0] == "equip":
            if len(words) < 2:
                print("You must specify an item to equip.")
            else:
                self.equip(words[1].upper())

        elif words[0] == "map":
            self.display_map(level)  # To be updated based on player class

        elif words[0] == "status":
            self.display_status()  # To be updated based on player class

        elif words[0] == "here":
            self.here()  # To be updated based on player class

        # Display help information about commands
        elif words[0] == "help":

            # Display command list
            if len(words) == 1:
                print("Commands: move, look, take, use, hunt, talk, trade, " +
                      "inventory, map, status, here, help")
                print("Items, Characters, and NPCs that can be interacted with"
                      + " are displayed in ALL CAPS.")

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
                print(
                    "Use the specified item. Optionally use item on specified target.")

            elif words[1] == "hunt":
                print("Usage: hunt")
                print("Hunt the Animal in the current room with the equipped weapon.")

            elif words[1] == "talk":
                print("Usage: talk")
                print("Talk to the Character in the current location.")

            elif words[1] == "trade":
                print("Usage: trade")
                print("Trade with the Character in the current location.")

            elif words[1] == "inventory":
                print("Usage: inventory")
                print("Display the player's equipped weapon and inventory.")

            elif words[1] == "map":
                print("Usage: map")
                print("Display the rooms the player has visited.")

            elif words[1] == "status":
                print("Usage: status")
                print("Display the player's status.")

            elif words[1] == "here":
                print("Usage: here")
                print("Display the description of current location.")

            elif words[1] == "equip":
                print("Usage: equip <weapon name>")
                print("Equip the specified weapon from the inventory.")

            elif words[1] == "help":
                print("Usage: help OR help <command>")
                print("Display command help information.")

            else:
                print("Commands: move, look, take, use, hunt, talk, trade, " +
                      "inventory, map, status, here, help")
                print("Items, Characters, and NPCs that can be interacted with"
                      + " are displayed in ALL CAPS.")

        else:
            print(
                "You didn't enter a valid command. Type \"help\" for a list of commands.")

        print("**************************************************")


def main():
    random.seed()
    level_1 = gen_random_level(10)
    meat = Consumable("MEAT", "A hunk of meat. Eat it to gain health.", 10, 1)
    mp = Consumable("MEDPACK", "A first aid kit that will fully restore your health.", 100, 1)
    hk = Weapon("KNIFE", "A plain hunting knife.", 10, 15)
    hunter = create_character("HUNTER",
                              "You see a <n> leaning against a nearby tree.",
                              "\"Hello there. If you have a <iw>, I'll trade you this <io> for it.\"",
                              copy.deepcopy(mp), copy.deepcopy(meat))
    bunny = Animal("BUNNY",
                   "There is a small space BUNNY hopping about nearby.",
                   16, 0.5, 5, copy.deepcopy(meat))
    level_1[0].character = hunter
    level_1[0].animal = bunny
    test_player = Player("Johnnie", level_1[0])
    test_player.add_item(copy.deepcopy(mp))
    test_player.add_item(copy.deepcopy(hk))
    while True:
        #       To test the mini map remove these comments:
        #
        # root = tk.Tk(className=" Example Gameplay")
        # root.config(bg='#3b444b')
        # root.geometry("880x660")
        # mapGUI.start_mini_map_IO(root, level_1[0])
        # root.mainloop()
        #
        # Then close it to continue with rest of main()

        test_player.get_user_input(level_1)


if __name__ == "__main__":
    main()