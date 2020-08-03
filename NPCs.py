from item import *
from random import randrange
from copy import deepcopy


class Character:
    def __init__(self, name, description, dialogue, item_offered, item_wanted):
        """
        Creates a Character object that can be placed in a Room and traded with.
        :param name: string user must enter to interact with the Character
        :param description: string that will be printed after Room description
        :param dialogue: string printed when user talks to the Character
        :param item_offered: item user will receive upon trading
        :param item_wanted: item user will lose upon trading
        """
        self._name = name
        self._description = description
        self._dialogue = dialogue
        self._item_offered = item_offered
        self._item_wanted = item_wanted
        self._trade_complete = False

    def get_name(self):
        return self._name

    def get_dialogue(self):
        return self._dialogue

    def get_description(self):
        return self._description

    def get_item_offered(self):
        return self._item_offered

    def get_item_wanted(self):
        return self._item_wanted

    def is_trade_complete(self):
        return self._trade_complete

    def set_trade_complete(self):
        self._dialogue = "\"Sorry, I have nothing left to trade.\""
        self._item_offered = None
        self._item_wanted = None
        self._trade_complete = True


def create_character(name, description, dialogue, item_offered, item_wanted):
    """
    Creates a Character class object. Enter <n> in description string to
    insert the Character's name. Enter <io> and <iw> in the dialogue string to
    insert the item names of the item_offered and item_wanted.
    :param name: string name of the character (i.e. "hunter", "trader", etc.)
    :param description: string that will be printed after Room description
    :param dialogue: string printed when user talks to the Character
    :param item_offered: item user will receive upon trading
    :param item_wanted: item user will lose upon trading
    :return: new Character object
    """
    char_name = str(name).upper()
    char_desc = description.replace("<n>", char_name)
    char_dial = dialogue.replace(
        "<io>", item_offered.get_name().upper()).replace(
        "<iw>", item_wanted.get_name().upper())
    char_io = item_offered
    char_iw = item_wanted

    return Character(char_name, char_desc, char_dial, char_io, char_iw)


class Animal:
    def __init__(self, name, description, health,
                 injure_chance, damage, reward):
        """
        Creates an Animal object that can be placed in a Room and hunted.
        :param name: string user must enter to interact with the Animal
        :param description: string that will be printed after Room description
        :param health: amount of damage that must be done to successfully hunt
        :param injure_chance: chance to injure Player when failing to kill
        :param damage: damage done to Player
        :param reward: item received upon successful hunt
        """
        self._name = name
        self._description = description
        self._health = health
        self._injure_chance = injure_chance
        self._damage = damage
        self._hunt_reward = reward

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_health(self):
        return self._health

    def get_injure_chance(self):
        return self._injure_chance

    def get_damage(self):
        return self._damage

    def get_hunt_reward(self):
        return self._hunt_reward

    def adj_health(self, integer):
        """
        Subtracts the given integer from the Animal's health.
        :param integer: number by which health is reduced
        :return:
        """
        self._health -= integer


def create_animal(name, description, health, injure_chance, damage, reward):
    """
    Creates an Animal class object. Enter <n> in description string to
    insert the Character's name.
    :param name: string name of the animal (i.e. "rabbit", "bear", etc.)
    :param description: string that will be printed after Room description
    :param health: amount of health the animal has (integer number)
    :param injure_chance: chance that animal will damage player during a hunt if
     its health is not depleted (float in range [0.0 .. 1.0))
    :param damage: damage to player if injured by the animal (integer number)
    :param reward: item received by player upon successfully hunting the animal
    :return: returns Animal class object
    """
    anml_name = str(name).upper()
    anml_desc = description.replace("<n>", anml_name)
    anml_reward = reward

    return Animal(anml_name, anml_desc, health,
                  injure_chance, damage, anml_reward)


# TODO: Expand and refine list.
character_master_list = [
    create_character("survivor",
                     "There is another <n> here.",
                     "Please, I need some <iw>. I can offer this <io> in return.",
                     create_meat(2), create_berries(1)),
    create_character("explorer",
                     "An alien <n> eyes you from a short distance away.",
                     "\"Greetings, traveller. I'm looking for a <iw>. If you're willing to trade, I'll give you this <io>.\"",
                     create_rations(2), create_meat(1)),
    create_character("trader",
                     "An alien <n> waves you over. It seems they want to make you an offer.",
                     "\"You look like you could use this <io>. I'd be willing to trade it for a <iw>.\"",
                     create_vitamins(2), create_meat(1)),
    create_character("warrior",
                     "An alien <n> signals to you that they want to talk.",
                     "\"You won't make it far without a decent weapon. If you get me a <iw>, I'll give you my <io>.\"",
                     create_axe(), create_vitamins(1)),
    create_character("doctor",
                     "A <n> from your ship's crew is here.",
                     "\"If you're hurt, I can give you this <io>, but I need a <iw> in return.\"",
                     create_medkit(1), create_meat(1))
]

# TODO: Expand and refine list.
animal_master_list = [
    create_animal("vermien",
                  "A small, relatively harmless <n> scurries about nearby, constantly watching you with one of its three eyes.",
                  10, 0.33, 5, create_meat(1)),
    create_animal("skevick",
                  "You spot a slithering <n>. It blends in well with the terrain.",
                  15, 0.50, 10, create_meat(1)),
    create_animal("boggu",
                  "A <n> growls at you from inside its den. You can see its eye glowing in the darkness.",
                  45, 0.40, 10, create_meat(2)),
    create_animal("eebrol", "A large <n> skitters toward you on its many short legs.",
                  50, 0.50, 10, create_meat(2)),
    create_animal("jabbin", "You see a large <n> sleeping nearby. It might be best not to wake it.",
                  55, 0.25, 20, create_meat(2)),
    create_animal("ixum",
                  "An eight-legged <n> crawls along the ground. You can see the venom glistening on its stingers.",
                  100, 0.33, 25, create_meat(3)),
    create_animal("mortrid", "A massive, horrifying <n> stands a short distance away. It opens its mouth and lets out a chilling screech!",
                  110, 0.50, 20, create_meat(3))
]


def gen_character(level_num):
    """
    Returns None or a random character object based on the given level_num number.
    """
    # 50% chance of returning character instead of None
    if randrange(0, 10) >= 5:

        # Later level_nums can spawn higher index characters
        if level_num + 1 > len(character_master_list):  # Prevent index o.o.b.
            range_max = len(character_master_list)
        else:
            range_max = level_num + 1

        if level_num - 3 < 0:
            range_min = 0
        else:
            range_min = level_num - 3

        char_index = randrange(range_min, range_max)

        return deepcopy(character_master_list[char_index])

    else:
        return None


def gen_animal(level_num):
    """
    Returns None or a random animal object based on the given level_num number.
    """
    # 50% chance of returning animal instead of None
    if randrange(0, 10) >= 5:

        # Later level_nums can spawn higher index animals
        if level_num + 1> len(animal_master_list):  # Prevent index o.o.b.
            range_max = len(animal_master_list)
        else:
            range_max = level_num + 1

        if level_num - 2 < 0:
            range_min = 0
        else:
            range_min = level_num - 2

        animal_index = randrange(range_min, range_max)

        return deepcopy(animal_master_list[animal_index])

    else:
        return None


# Test animal and character generation.

# for i in range(0, 10):
#     character = gen_character(4)
#     animal = gen_animal(4)
#     if character is not None:
#         char_name = character.get_name()
#     else:
#         char_name = "None"
#     if animal is not None:
#         anml_name = animal.get_name()
#     else:
#         anml_name = "None"
#     print(char_name + ", " + anml_name)
