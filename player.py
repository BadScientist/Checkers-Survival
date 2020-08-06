from room import *
from mapGUI import start_large_map_IO

# FIXME: "Map" command doesn't clear from the textbox. Doesn't act like other
#  commands.


# example use of functions below class definition
class Player:
    def __init__(self, disp_func):
        """
        Initializes a Player class object.
        :param disp_func: Function to print strings to the interface.
        """
        self._health = 100
        self.location = None
        self._weapon = create_knife()
        self._inventory = [create_medkit(1)]
        self.i_print = disp_func

    def is_game_over(self):
        """
        Returns false if the player's health is greater than 0, otherwise
        returns true.
        """
        return self._health <= 0

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
            self.i_print("You didn't enter a valid direction.")
            return

        # No adjacent room error message
        if adj_room is None:
            self.i_print("You can't go that way.")
            return
        else:
            event = self.location.get_event()
            if event is not None:
                self._health -= event()
            adj_room.apply_seen()  # To view adjacent room contents in Maps
            self.location = adj_room

            # Check if player was killed by event.
            if not self.is_game_over():
                self.here()

    def here(self):
        """
        Displays the long_desc of the Room that is currently set as the Player's
        location.
         """
        # Print current room's long description
        self.i_print(self.location.get_long_desc())

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
            self.i_print("You didn't enter a valid direction.")
            return

        # No adjacent room error message
        if adj_room is None:
            self.i_print("There is nothing in that direction.")
            return
        else:
            adj_room.apply_seen()  # To view adjacent room contents in Maps
            self.i_print("To the " + dir_str + " you see " + adj_room.get_shrt_desc())

    def set_start_position(self, start_room):
        start_room.apply_seen()
        self.location = start_room

    def add_item(self, new_item):
        """Add the given item to the inventory."""

        # If the item is a Consumable, check if the player already has the same
        # item. If so, add the use count to the new item, remove the current
        # item from the inventory, and then add the new item.
        if new_item.get_type() == "CONSUMABLE":
            for item in self._inventory:
                if item.get_name() == new_item.get_name():
                    new_item.adj_use_count(item.get_use_count())
                    self._inventory.remove(item)

        # Add the new item to the inventory.
        self._inventory.append(new_item)

    def take(self):
        """Add the item in the room to the inventory."""
        item = self.location.get_item()
        if item is not None:
            self.add_item(item)
            self.location.remove_item()
            self.i_print("You picked up the " + item.get_name() + '.')
        else:
            self.i_print("There is nothing here to take.")

    def use(self, item_str):
        """Use the specified consumable item."""

        # Check if the specified item is in the inventory.
        for item in self._inventory:
            if item.get_name() == item_str.upper():

                # Check if the item is a consumable.
                if item.get_type() != "CONSUMABLE":
                    self.i_print("You can't use that.")

                else:
                    # Adjust the player's health and item's use count.
                    self._health += item.get_health_gein()

                    # Make sure current health doesn't exceed maximum of 100.
                    if self._health > 100:
                        self._health = 100

                    item.use_item()

                    # Remove item from inventory if no more uses.
                    if not item.usable():
                        self._inventory.remove(item)

                    self.i_print("You used " + item.get_name() + ".")
                    return

        self.i_print("You don't have that.")

    def hunt(self):
        """Hunt the animal in the current location with the equipped weapon."""
        weapon = self._weapon
        animal = self.location.get_animal()

        if animal is None:
            self.i_print("There is nothing here to hunt.")
            return

        if weapon is None:
            self.i_print("You must equip a weapon to hunt.")
            return

        # Reduce the animal's health by an amount
        # in the equipped weapon's damage range
        dmg = int(weapon.rand_dmg())
        animal.adj_health(dmg)
        self.i_print("You attack the " + animal.get_name() + " with your " +
              weapon.get_name() + ".")

        # Check if animal has health remaining. If not, give player the reward,
        # print success message, and remove animal from room.
        if animal.get_health() <= 0:
            reward = animal.get_hunt_reward()
            self.add_item(reward)
            self.i_print("You killed the " + animal.get_name() + " and got " +
                  reward.get_name() + ".")
            self.location.remove_animal()

        # If animal still has health, print message notifying player.
        else:
            self.i_print("You hurt the " + animal.get_name() +
                  ", but it's still alive.")

            # Check if animal injures player. If so, reduce player's health by
            # animal's damage and print message notifying player.
            if random() < animal.get_injure_chance():
                self._health -= animal.get_damage()
                self.i_print("You were hurt by the " + animal.get_name())

    def talk(self):
        """
        Talk to the Character in the Room in which the Player is located.
        """
        character = self.location.get_character()
        if character is not None:
            self.i_print("The " + character.get_name() + " greets you:")
            self.i_print(self.location.get_character().get_dialogue())

        else:
            self.i_print("There is no one here to talk to.")

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

                        # Add the item_offered to the inventory.
                        self.add_item(item_offered)

                        # Remove 1 count of the traded item from the inventory.
                        # If no more uses, remove the item from the inventory.
                        item1.adj_use_count(-1)
                        if item1.get_use_count() < 1:
                            self._inventory.remove(item1)

                        character.set_trade_complete()
                        self.i_print("You hand the " + character.get_name() + " the " +
                              item_wanted.get_name() + " and they give you a " +
                              item_offered.get_name() + " in return.")
                        self.i_print("\"Thanks for the trade.\"")
                        return

                self.i_print("You don't have the correct item to trade.")

            else:
                self.i_print("\"Sorry, I have nothing left to trade.\"")

        else:
            self.i_print("There is no one here to trade with.")

    def display_inventory(self):
        self.i_print("Equipped Weapon:\n-", self._weapon, "\n\nInventory:")
        if len(self._inventory) == 0:
            self.i_print("Your inventory is empty.")
        else:
            for item in self._inventory:
                self.i_print("-", item)

    def display_map(self, level):
        start_large_map_IO(level, self.location)
        self.i_print("You look at your map.")

    def display_status(self):
        self.i_print("Health: " + str(self._health) + "/100")

    # set functions
    def adj_health(self, amount):
        """Adjusts the player's health by the given amount."""
        self._health += amount

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
                    self.i_print("You can't equip that.")
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
            self.i_print("You don't have a " + weapon_str + " in your inventory.")

    # get functions
    def get_health(self):
        return self._health

    def get_weapon(self):
        return self._weapon

    def get_item(self, item_num):
        return self._inventory[item_num]

    def get_location(self):
        return self.location

    def get_user_input(self, level, text):

        # Get input. Prompt is placeholder.
        curr_input = text
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
                self.i_print("You must specify a valid direction to move.")
            else:
                self.move(words[1])  # To be updated based on player class

        elif words[0] == "look":
            if len(words) == 1:
                self.i_print("You must specify a valid direction to look.")
            else:
                self.look(words[1])  # To be updated based on player class

        elif words[0] == "take":
            self.take()  # To be updated based on player class

        elif words[0] == "use":

            if len(words) == 1:
                self.i_print("You must specify a valid item to use.")

            # Use item.
            else:
                self.use(words[1])  # To be updated based on player class

        elif words[0] == "hunt":
            self.hunt()  # To be updated based on player class

        elif words[0] == "talk":
            self.talk()  # To be updated based on player class

        elif words[0] == "trade":
            self.trade()

        elif words[0] == "inventory":
            self.display_inventory()  # To be updated based on player class

        elif words[0] == "equip":
            if len(words) < 2:
                self.i_print("You must specify an item to equip.")
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
                self.i_print("Commands: move, look, take, use, hunt, talk, trade, " +
                      "inventory, map, status, here, help")
                self.i_print("Items, Characters, and NPCs that can be interacted with"
                      + " are displayed in ALL CAPS.")

            elif words[1] == "move":
                self.i_print("Usage: move <direction>")
                self.i_print("Move to the location in the specified direction.")

            elif words[1] == "look":
                self.i_print("Usage: look <direction>")
                self.i_print("Look in the specified direction.")

            elif words[1] == "take":
                self.i_print("Usage: take")
                self.i_print("Take the item in the current location.")

            elif words[1] == "use":
                self.i_print("Usage: use <item>")
                self.i_print("Use the specified consumable item.")

            elif words[1] == "hunt":
                self.i_print("Usage: hunt")
                self.i_print("Hunt the Animal in the current" +
                      "location with the equipped weapon.")

            elif words[1] == "talk":
                self.i_print("Usage: talk")
                self.i_print("Talk to the Character in the current location.")

            elif words[1] == "trade":
                self.i_print("Usage: trade")
                self.i_print("Trade with the Character in the current location.")

            elif words[1] == "inventory":
                self.i_print("Usage: inventory")
                self.i_print("Display the player's equipped weapon and inventory.")

            elif words[1] == "map":
                self.i_print("Usage: map")
                self.i_print("Display the rooms the player has visited.")

            elif words[1] == "status":
                self.i_print("Usage: status")
                self.i_print("Display the player's status.")

            elif words[1] == "here":
                self.i_print("Usage: here")
                self.i_print("Display the description of current location.")

            elif words[1] == "equip":
                self.i_print("Usage: equip <weapon name>")
                self.i_print("Equip the specified weapon from the inventory.")

            elif words[1] == "help":
                self.i_print("Usage: help OR help <command>")
                self.i_print("Display command help information.")

            else:
                self.i_print("Commands: move, look, take, use, hunt, talk, trade, " +
                      "inventory, map, status, here, help")
                self.i_print("Items, Characters, and NPCs that can be interacted with"
                      + " are displayed in ALL CAPS.")

        else:
            self.i_print(
                "You didn't enter a valid command." +
                "Type \"help\" for a list of commands.")

        self.i_print("**************************************************")
