from room import *
from mapGUI import start_large_map_IO
from tkinter import *


class Player:
    def __init__(self, canvas):
        self._health = 100
        self.location = None
        self._minutes_passed = 0
        self._weapon = create_knife()
        self._inventory = [create_medkit(1)]
        self.canvas = canvas  # the UI
        
    def print_prompt(self, value):
        dialogleft = Canvas(self.canvas, bg="#bbbbbb", width=550, height=600,
                            highlightthickness=3, highlightbackground="black")
        prompt = Text(dialogleft, height=35, width=65, bg="#bbbbbb", 
                      highlightthickness=0)
        prompt.config(state=NORMAL)
        prompt.insert(END, value)
        prompt.config(state=DISABLED)
        dialogleft.pack()
        prompt.pack()
        self.canvas.create_window(300, 325, window=dialogleft)
    
    def is_game_over(self):
        return self._health <= 0

    def make_health_nonnegative(self):
        if self._health < 0:
            self._health = 0
   
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
            self.print_prompt("You didn't enter a valid direction.")
            return

        # No adjacent room error message
        if adj_room is None:
            self.print_prompt("You can't go that way.")
            return
        else:
            event = self.location.get_event()
            if event is not None:
                self._health -= event()
                self.make_health_nonnegative()
                self.location.remove_event()
            adj_room.apply_seen()  # To view adjacent room contents in Maps
            self.location = adj_room

            # Check if player was killed by event.
            if not self.is_game_over():
                self._minutes_passed += 240
                self.here()

    def here(self):
        self.print_prompt(self.location.get_long_desc())

    def look(self, dir_str):
        """
        Displays the short description of the room in the given direction, if
        present.
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
            self.print_prompt("You didn't enter a valid direction.")
            return

        # No adjacent room error message
        if adj_room is None:
            self.print_prompt("There is nothing in that direction.")
            return
        else:
            adj_room.apply_seen()  # To view adjacent room contents in Maps
            self.print_prompt("To the " + dir_str + " you see " +
                              adj_room.get_shrt_desc())
    
    def set_start_position(self, start_room):
        start_room.apply_seen()
        self.location = start_room
    
    def add_item(self, new_item):
        """Add the given item to the inventory."""
        for item in self._inventory:
            if item.get_name() == new_item.get_name():
                # Add existing use count to new item use count
                if new_item.get_type() == "CONSUMABLE":
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
            self._minutes_passed += 15
            self.print_prompt("You picked up the " + item.get_name() + '.')
        else:
            self.print_prompt("There is nothing here to take.")

    def use(self, item_str):
        """Use the specified consumable item."""

        # Check if the specified item is in the inventory.
        for item in self._inventory:
            if item.get_name() == item_str.upper():

                # Check if the item is a consumable.
                if item.get_type() != "CONSUMABLE":
                    self.print_prompt("You can't use that.")

                else:
                    # Adjust the player's health and item's use count.
                    self.adj_health(item.get_health_gein())

                    item.use_item()

                    # Remove item from inventory if no more uses.
                    if not item.usable():
                        self._inventory.remove(item)

                    self.print_prompt("You used " + item.get_name() + ".")
                    self._minutes_passed += 15
                    return

        self.print_prompt("You don't have that.")

    def hunt(self):
        """Hunt the animal in the current location with the equipped weapon."""
        weapon = self._weapon
        animal = self.location.get_animal()

        if animal is None:
            self.print_prompt("There is nothing here to hunt.")
            return

        if weapon is None:
            self.print_prompt("You must equip a weapon to hunt.")
            return

        # Reduce the animal's health by an amount in equipped weapon's dmg range
        dmg = int(weapon.rand_dmg())
        animal.adj_health(dmg)
        hunt_string = "You attack the " + animal.get_name() + " with your " + \
                      weapon.get_name() + ".\n"

        # If animal has no health remaining, give player the reward,
        # print success message, and remove animal from room.
        if animal.get_health() <= 0:
            reward = animal.get_hunt_reward()
            self.add_item(reward)
            hunt_string += "You killed the " + animal.get_name() + \
                           " and got " + reward.get_name() + "."
            self.location.remove_animal()

        # If animal still has health, print message notifying player.
        else:
            hunt_string += "You hurt the " + animal.get_name() + \
                           ", but it's still alive.\n"

            # If animal injures player, reduce player's health by
            # animal's damage and print message notifying player.
            if random() < animal.get_injure_chance():
                self._health -= animal.get_damage()
                self.make_health_nonnegative()
                hunt_string += "You were hurt by the " + animal.get_name()

        self._minutes_passed += 120
        self.print_prompt(hunt_string)

    def talk(self):
        """
        Talk to the Character in the Room in which the Player is located.
        """
        character = self.location.get_character()
        if character is not None:
            self.print_prompt("The " + character.get_name() + " greets you:\n" +
                              self.location.get_character().get_dialogue())
            self._minutes_passed += 15

        else:
            self.print_prompt("There is no one here to talk to.")

    def trade(self):
        """
        Trade with the Character in the Room in which the Player is located.
        """
        character = self.location.get_character()

        if character is not None:
            item_wanted = character.get_item_wanted()
            item_offered = character.get_item_offered()
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
                        self.print_prompt("You hand the " +
                                          character.get_name() + " the " +
                                          item_wanted.get_name() +
                                          " and they give you a " +
                                          item_offered.get_name() +
                                          " in return.\n\"Thanks for the " +
                                          "trade.\"")
                        self._minutes_passed += 15
                        return

                self.print_prompt("You don't have the correct item to trade." +
                                  "\n\nCorrect item: " + item_wanted.get_name())

            else:
                self.print_prompt("\"Sorry, I have nothing left to trade.\"")

        else:
            self.print_prompt("There is no one here to trade with.")

    def display_inventory(self):
        inventory_string = "Equipped Weapon:\n- " + str(self._weapon) + \
                           "\n\nInventory:\n"
        if len(self._inventory) == 0:
            inventory_string += "Your inventory is empty."
        else:
            for item in self._inventory:
                inventory_string += "- " + str(item) + "\n"
        self.print_prompt(inventory_string)

    def display_map(self, level):
        start_large_map_IO(level, self.location)
        self.print_prompt("You look at your map.")

    def display_status(self):
        self.print_prompt("Health: " + str(self._health) + "/100")

    def adj_health(self, amount):
        self._health += amount
        if self._health >= 100:
            self._health = 100
            
    def equip(self, weapon_str):
        """
        Exchange the equipped weapon for the specified weapon in the inventory.
        :param weapon_str: user input string from get_player_input
        """
        weapon = None

        # Search for specified weapon in inventory.
        for item in self._inventory:
            if item.get_name() == weapon_str:

                # Check that the item is a weapon.
                if item.get_type() != "WEAPON":
                    self.print_prompt("You can't equip that.")
                    return

                weapon = item
                self._inventory.remove(item)
                break

        # If present, exchange inventory weapon for equipped weapon.
        if weapon is not None:
            if self._weapon is not None:
                self._inventory.append(self._weapon)
            self._weapon = weapon
            self._minutes_passed += 15
            self.display_inventory()

        else:
            self.print_prompt("You don't have a " + weapon_str +
                              " in your inventory.")

    def get_health(self):
        return self._health

    def get_inventory(self):
        items = []
        for item in self._inventory:
            items.append(item)
        if self._weapon not in items:
            items.append(self._weapon)
        return items

    def get_weapon(self):
        return self._weapon

    def get_item(self, item_num):
        return self._inventory[item_num]
    
    def get_location(self):
        return self.location

    def get_time(self):
        """
        Returns the time passed in game as a string in the form "Day D, HH:MM"
        """
        total_minutes = self._minutes_passed
        clock_minutes = str(total_minutes % 60)
        if len(clock_minutes) == 1:
            clock_minutes = "0" + clock_minutes

        total_hours = total_minutes // 60
        clock_hours = str(total_hours % 24)
        if len(clock_hours) == 1:
            clock_hours = "0" + clock_hours

        days = str((total_hours // 24) + 1)

        date_time = "Day " + days + ", " + clock_hours + ":" + clock_minutes

        return date_time

    def get_user_input(self, level, text):

        curr_input = text
        words = []
        curr_word = ""

        for letter in curr_input.lower():
            if letter != ' ':
                curr_word += letter
            else:
                words.append(curr_word)
                curr_word = ""

        words.append(curr_word)  # Add final word to list

        # Call methods based on user input.
        if words[0] == "move":
            if len(words) == 1:
                self.print_prompt("You must specify a valid direction to move.")
            else:
                self.move(words[1])

        elif words[0] == "look":
            if len(words) == 1:
                self.print_prompt("You must specify a valid direction to look.")
            else:
                self.look(words[1])

        elif words[0] == "take":
            self.take()

        elif words[0] == "use":

            if len(words) == 1:
                self.print_prompt("You must specify a valid item to use.")

            # Use item.
            else:
                self.use(words[1])

        elif words[0] == "hunt":
            self.hunt()

        elif words[0] == "talk":
            self.talk()

        elif words[0] == "trade":
            self.trade()

        elif words[0] == "inventory":
            self.display_inventory()

        elif words[0] == "equip":
            if len(words) < 2:
                self.print_prompt("You must specify an item to equip.")
            else:
                self.equip(words[1].upper())

        elif words[0] == "map":
            self.display_map(level)

        elif words[0] == "status":
            self.display_status()

        elif words[0] == "here":
            self.here()

        # Display help information about commands
        elif words[0] == "help":

            general_help = "Commands: move, look, take, use, hunt, talk, trad" \
                           "e, inventory,\nmap, status, here, help\nEnter \"h" \
                           "elp\" followed by another command for instruction" \
                           "s on\nusing the command.\nItems, Characters, and " \
                           "NPCs that can be interacted with are\ndisplayed i" \
                           "n ALL CAPS."

            if len(words) == 1:
                self.print_prompt(general_help)

            elif words[1] == "move":
                self.print_prompt("Usage: move <direction>\nMove to the " +
                                  "location in the specified direction." +
                                  "\nValid directions are north, south, east," +
                                  " and west (or n, s, e,\nand w).")

            elif words[1] == "look":
                self.print_prompt("Usage: look <direction>\nLook in the " +
                                  "specified direction.\nValid directions " +
                                  "are north, south, east, and west (or n, " +
                                  "s, e,\nand w).")

            elif words[1] == "take":
                self.print_prompt("Usage: take\nTake the item in the current " +
                                  "location.")

            elif words[1] == "use":
                self.print_prompt("Usage: use <item>\nUse the specified " +
                                  "consumable item.")

            elif words[1] == "hunt":
                self.print_prompt("Usage: hunt\nHunt the Animal in the " +
                                  "current location with the equipped weapon.")

            elif words[1] == "talk":
                self.print_prompt("Usage: talk\nTalk to the Character in the" +
                                  " current location.")

            elif words[1] == "trade":
                self.print_prompt("Usage: trade\nTrade with the Character in " +
                                  "the current location.")

            elif words[1] == "inventory":
                self.print_prompt("Usage: inventory\nDisplay the player's " +
                                  "equipped weapon and inventory.")

            elif words[1] == "map":
                self.print_prompt("Usage: map\nDisplay the rooms the player " +
                                  "has visited.")

            elif words[1] == "status":
                self.print_prompt("Usage: status\nDisplay the player's status.")

            elif words[1] == "here":
                self.print_prompt("Usage: here\nDisplay the description of " +
                                  "current location.")

            elif words[1] == "equip":
                self.print_prompt("Usage: equip <weapon name>\nEquip the " +
                                  "specified weapon from the inventory.")

            elif words[1] == "help":
                self.print_prompt("Usage: help OR help <command>\nDisplay " +
                                  "command help information.")

            else:
                self.print_prompt(general_help)

        else:
            self.print_prompt(
                "You didn't enter a valid command.\n" +
                "Type \"help\" for a list of commands.")
