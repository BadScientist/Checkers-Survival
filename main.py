import random


# example use of functions below class definition

class Room:
    # Variables:
    #   long_desc -> printed in-game when within the room
    #   shrt_desc -> printed in-game when in a room adjacent to this room
    #   N,S,E,W   -> point to adjacent room in respective direction (in 2D)
    #                set to None (null) if not yet defined

    def __init__(self, long_desc=None, shrt_desc=None, n=None, s=None, e=None,
                 w=None):
        self.long_desc = long_desc
        self.shrt_desc = shrt_desc
        self.N = n
        self.S = s
        self.E = e
        self.W = w

    def get_n(self):
        return self.N

    def get_s(self):
        return self.S

    def get_e(self):
        return self.E

    def get_w(self):
        return self.W

    def apply_long(self, long_desc):
        self.long_desc = long_desc

    def apply_shrt(self, shrt_desc):
        self.shrt_desc = shrt_desc

    def apply_path(self, direction, target):
        # direction eg N, S ...; target is the room path leads to
        # check if path already occupied and if there's existing path to target
        if self != target:
            if self.get_adjacent_room(direction) is None:
                all_paths = ['N', 'S', 'E', 'W']
                for path in all_paths:
                    if getattr(self, path) == target:
                        return False  # failure
                setattr(self, direction, target)
                return True
            else:
                return False
        else:
            return False

    def get_long_desc(self):
        return self.long_desc

    def get_shrt_desc(self):
        return self.shrt_desc

    def get_adjacent_room(self, direction):
        # direction eg N, S ...;
        return getattr(self, direction)

    def get_empty_paths(self):  # used for level generation
        # get all paths/directions that don't have an assigned room
        # returns an array of all available paths
        all_paths = ['N', 'S', 'E', 'W']
        idx = 0
        while idx < len(all_paths):
            direction = all_paths[idx]
            if getattr(self, direction) is not None:
                all_paths.remove(direction)
                idx -= 1
            idx += 1
        return all_paths


class Player:
    def __init__(self, name, start_room, weapon):
        self._name = name
        self._health = 100
        self.location = start_room
        self._weapon = weapon
        self._inventory = []

    def move(self, dir_str):
        """
        Updates the player's location to the adjacent room in the given
        direction (if present) and displays the long_desc of the new room.
        """
        # Get the room in the given direction
        if dir_str == 'n' or dir_str == "north":
            adj_room = self.location.get_n()

        elif dir_str == 's' or dir_str == "south":
            adj_room = self.location.get_s()

        elif dir_str == 'e' or dir_str == "east":
            adj_room = self.location.get_e()

        elif dir_str == 'w' or dir_str == "west":
            adj_room = self.location.get_w()

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
            adj_room = self.location.get_n()

        elif dir_str == 's' or dir_str == "south":
            adj_room = self.location.get_s()

        elif dir_str == 'e' or dir_str == "east":
            adj_room = self.location.get_e()

        elif dir_str == 'w' or dir_str == "west":
            adj_room = self.location.get_w()

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


def create_path(parent, target, paths):
    # parent is the existing room the new room (target) will be joined to
    # only possible reason for failure is the parent's paths are filled
    opposite_dir = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }
    if paths:
        idx = random.randint(0, len(paths) - 1)
        direction = paths[idx]
        if parent.apply_path(direction, target) is False:
            return False
        else:
            return target.apply_path(opposite_dir[direction], parent)
    else:
        return False


def gen_random_level(room_num):
    # creates a room at a time, joining the new room (target) to the existing
    # 'bunch' of rooms. Joins to a specific 'parent'
    all_rooms = []
    avail_rooms = []  # has index of rooms with an available path
    for i in range(0, room_num):
        long_desc = "Room " + str(i) + "'s long description."
        shrt_desc = "Room " + str(i) + "'s short description."
        all_rooms.append(Room(long_desc, shrt_desc))  # create the new room (target)
        avail_rooms.append(i)
        if i == 0:
            continue
        flag = False
        while not flag:
            if i == 1:  # 2 rooms only
                parent = all_rooms[0]
                avail_paths = parent.get_empty_paths()  # parent's available paths
                flag = create_path(parent, all_rooms[i], avail_paths)
            if i > 1:  # more than 2 rooms
                idx = random.randint(0, len(avail_rooms) - 2)
                parent = all_rooms[avail_rooms[idx]]
                avail_paths = parent.get_empty_paths()  # parent's available paths
                flag = create_path(parent, all_rooms[i], avail_paths)
            if not flag:
                avail_rooms.remove(idx)  # remove room from 'bunch'-paths filled
                # print('room Filled! Fail!')
    # for i in range(0, room_num):
    #   print(all_rooms[i].__dict__)
    #   print('')
    # print(avail_rooms)
    return all_rooms


def main():
    level_1 = gen_random_level(10)
    test_player = Player("Johnnie", level_1[0], "hunting knife")
    while True:
        test_player.get_user_input()

# print(room_1.get_long_desc())
# print(room_1.get_shrt_desc())

# room_1.apply_long('goin don know')
# room_1.apply_path('N', room_2)

# print(room_1.__dict__)
# to print all class vars


if __name__ == "__main__":
    main()
