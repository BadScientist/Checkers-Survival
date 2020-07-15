class Player:
    def __init__(self, name, weapon):
        self._name = name
        self._health = 100
        self._weapon = weapon
        self._inventory = []

    def move(self, str):
        print("Moved " + str)

    def look(self, str):
        print("Looked " + str)

    def take(self, str):
        print("Took " + str)

    def use(self, str1, str2=None):
        if str2 is None:
            print("Used " + str1)
        else:
            print("Used " + str1 + " on " + str2)

    def hunt(self, str1, str2):
        print("Hunted " + str1 + " with " + str2)

    def talk(self, str):
        print("Talked to " + str)

    def trade(self, str):
        print("Traded your item for " + str + "'s other item.")

    #set funcitons
    def set_health(self, health):
        self._health = health
    def add_item(self, item):
        self._inventory.append(item)
    def set_weapon(self, weapon):
        self._weapon = weapon
               
    #get functions
    def get_health(self):
        return self._health
    def get_weapon(self):
        return self._weapon
    def get_item(self, item_num):
        return self._inventory[item_num]
        
def get_user_input(player_obj):

    curr_input = input("Test prompt: ")  # Get input. Prompt is placeholder.
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
            player_obj.move(words[1])  # To be updated based on player class

    elif words[0] == "look":
        if len(words) == 1:
            print("You must specify a valid direction to look.")
        else:
            player_obj.look(words[1])  # To be updated based on player class

    elif words[0] == "take":
        if len(words) == 1:
            print("You must specify a valid item to take.")
        else:
            player_obj.take(words[1])  # To be updated based on player class

    elif words[0] == "use":

        if len(words) == 1:
            print("You must specify a valid item to use.")

        # Use item.
        elif len(words) == 2:
            player_obj.use(words[1])  # To be updated based on player class

        # Use item on target.
        else:
            player_obj.use(words[1], words[2])  # To be updated based on player class

    elif words[0] == "hunt":

        if len(words) < 3:
            print("You must specify a target and a weapon to use.")

        # Hunt target with weapon.
        else:
            player_obj.hunt(words[1], words[2])  # To be updated based on player class

    elif words[0] == "talk":

        if len(words) < 2:
            print("You must specify who you want to talk to.")

        else:
            player_obj.talk(words[1])  # To be updated based on player class

    elif words[0] == "trade":

        if len(words) < 2:
            print("You must specify who you with to trade with.")

        else:
            player_obj.trade(words[1])

    elif words[0] == "inventory":
        player_obj.display_inventory()  # To be updated based on player class

    elif words[0] == "map":
        player_obj.display_map()  # To be updated based on player class

    elif words[0] == "status":
        player_obj.display_status()  # To be updated based on player class

    elif words[0] == "here":
        player_obj.display_location()  # To be updated based on player class

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


# player = Player()

# while True:
#    get_user_input(player)