from item import *


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
    Creates a Character class object. Enter <n> to in description string to
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

    return Character(char_name, char_desc, char_dial, item_offered, item_wanted)


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

# meat = Consumable("meat", "A hunk of meat. Eat it to gain health.", 10, 1)
# hp = Consumable("health pack", "A first aid kit that will fully restore your health.", 100, 1)

# mychar = create_character("hunter",
#                          "You see a <n> leaning against a nearby tree.",
#                          "\"Hello there. If you have a <iw>, I'll trade you this <io> for it.\"",
#                          hp, meat)

# print(mychar.get_name())
# print(mychar.get_dialogue())
# print(mychar.get_description())
