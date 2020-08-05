from random import randrange


def cave_in():
    print("The ground begins to shake beneath your feet. Thinking quickly, " +
          "you...\n\n1 - dive forward.\n2 - stand still.\n3 - roll " +
          "backwards.\n\nEnter the number of the action you want to perform.")

    choice = input()

    while choice not in ["1", "2", "3"]:
        print("You must enter the number of one of the options.")
        choice = input()

    if choice == "2":
        print("The ground caves in beneath your feet and you fall into a " +
              "sinkhole! You were injured by the fall.")
        return -10

    else:
        print("You move out of the way just before the ground caves " +
              "in!\nYou continue on your way without injury.")
        return 0


def creature_attack():
    print("You hear a slight crunch behind you. You...\n\n1 - turn around " +
          "slowly.\n2 - keep walking.\n3 - quickly pull out you weapon and " +
          "turn around.\n\nEnter the number of the action you want to perform.")

    choice = input()

    while choice not in ["1", "2", "3"]:
        print("You must enter the number of one of the options.")
        choice = input()

    if choice == "3":
        print("A huge jabbin tries to lunge at you, but you strike it just " +
              "in time! The injured creature runs away.\nYou continue on " +
              "your way without injury.")
        return 0

    else:
        print("You are pounced on by a huge jabbin! You manage to fight it " +
              "off, but not before it injures you.")
        return 20


def poison_cloud():
    print("You smell something strange. It keeps getting stronger as you " +
          "walk. You...\n\n1 - cover your nose and mouth with your hand.\n2 " +
          "- move to higher ground.\n3 - hold your breath.\n\nEnter the " +
          "number of the action you want to perform.")

    choice = input()

    while choice not in ["1", "2", "3"]:
        print("You must enter the number of one of the options.")
        choice = input()

    if choice == "1":
        print("Noxious gas leaks through your fingers, poisoning you!")
        return 10

    elif choice == "2":
        print("You manage to make it to a hilltop just before a noxious cloud" +
              " fills the low ground around you!\nOnce the cloud dissipates, " +
              "you continue on without injury.")
        return 0

    else:
        print("You hold your breath as long as you can, but eventually you " +
              "have to breath. You inhale a large amount of noxious gas!")
        return 20


def flood():
    print("You hear a rumbling noise in the distance. The sound keeps getting" +
          " loader and louder. You...\n\n1 - turn toward the sound and wait." +
          "\n2 - dive forward.\n3 - move to higher ground.\n\nEnter the " +
          "number of the action you want to perform.")

    choice = input()

    while choice not in ["1", "2", "3"]:
        print("You must enter the number of one of the options.")
        choice = input()

    if choice == "1":
        print("A flash flood rushes in and knocks you off your feet! You are " +
              "battered by debris, but manage not to drown by clinging to the" +
              " flotsam.")
        return 15

    elif choice == "2":
        print("You try to dive out of the way, but it does you no good as a " +
              "flash flood rushes over you! You are battered by debris, but " +
              "manage not to drown by clinging to the flotsam.")
        return 15

    else:
        print("You manage to make it to a hilltop just before a flash flood " +
              "fills the low ground around you!\nOnce the water recedes, " +
              "you continue on without injury.")
        return 0


def storm():
    print("Clouds begin to gather in the sky above you. As it gets darker " +
          "and darker, you decide to...\n\n1 - find shelter.\n2 - move to " +
          "higher ground.\n3 - keep moving.\n\nEnter the number of the " +
          "action you want to perform.")

    choice = input()

    while choice not in ["1", "2", "3"]:
        print("You must enter the number of one of the options.")
        choice = input()

    if choice == "1":
        print("You manage to find shelter in a shallow cave just before a " +
              "massive storm hits.\nYou wait for the storm to pass before " +
              "moving on unharmed.")
        return 0

    elif choice == "2":
        print("You make it to a hilltop just as a massive storm hits. Being " +
              "so high up only puts you in more danger as\nlightning strikes " +
              "right next to you! You aren't hit directly, but you are still " +
              "injured by the blast.")
        return 20

    else:
        print("As you continue on, a massive storm hits! The powerful winds " +
              "batter you with debris, injuring you.")
        return 10


event_master_list = [cave_in, creature_attack, poison_cloud, flood, storm]


def gen_event():
    """
    Returns None or a random event function based on the given level_num number.
    """
    # 20% chance of returning character instead of None
    if randrange(0, 5) == 4:
        return event_master_list[randrange(0, len(event_master_list))]

    else:
        return None


# test = gen_event()
#
# if test is not None:
#     test()
# else:
#     print("None")
