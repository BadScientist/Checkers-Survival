def get_user_input(player_obj):

    curr_input = input()  # Get input. Currently no prompt.
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

    elif words[0] == "inventory":
        player_obj.display_inventory()  # To be updated based on player class

    elif words[0] == "map":
        player_obj.display_map()  # To be updated based on player class

    elif words[0] == "status":
        player_obj.display_status()  # To be updated based on player class