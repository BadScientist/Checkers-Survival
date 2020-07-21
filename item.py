import random

print("test file")  # testing if file works


class Item:
    """Item class of the game."""
    def __init__(self, name, str_desc, type):
        """Creates an  item object.\n
        parameters: name, str_desc"""
        self._name = name
        self._str_desc = str_desc
        self._type = type
    
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

    def get_type(self):
        return self._type

    def __str__(self):
        return self._name + ": " + self._str_desc


class Weapon(Item):
    """Weapon class of the game."""
    def __init__(self, name, str_desc, dmg_low, dmg_high):
        """Creates a weapon object.\n
        parameters: name, str_desc, dmg_low, dmg_high"""
        self._name = name
        self._str_desc = str_desc
        self._type = "WEAPON"
        self._dmg_low = dmg_low
        self._dmg_high = dmg_high
    
    def __str__(self):
        return self._name + ": " + self._str_desc + " low: " + str(self._dmg_low) + ", high:" + str(self._dmg_high) 
    
    def rand_dmg(self):
        """
        Returns randomized dmg value between dmg low and dmg_high (inclusive).
        """
        return random.randrange(self._dmg_low, self._dmg_high + 1)

    def get_low(self):
        """Returns low range of damage."""
        return self._dmg_low
    
    def get_high(self):
        """Returns high range of damage."""
        return self._dmg_high


class Consumable(Item):
    """Consumable class in game."""
    def __init__(self, name, str_desc, value, use_count):
        """Creates a consumable object.\n
        parameters: name, str_desc, value, use_count"""
        self._name = name
        self._str_desc = str_desc
        self._type = "CONSUMABLE"
        self._value = value
        self._use_count = use_count

    def __str__(self):
        return self._name + ": " + self._str_desc + " value: " + str(self._value) + ", use count:" + str(self._use_count) 
        
    def get_value(self):
        """get the value of the consumable."""
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
    
    def adj_use_count(self, integer):
        """Adjusts the consumable item use count by the given integer."""
        self._use_count += integer