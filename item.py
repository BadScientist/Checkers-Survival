import random

# =============================================================================
# use functions below the classes to initialize an item
# there are specific functions e.g create_knife to create standard items
# =============================================================================


# TODO: adjust the attributes of the items e.g. damage and use_count

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


def create_weapon(name, str_desc, dmg_low, dmg_high):
    return Weapon(name, str_desc, dmg_low, dmg_high)


def create_knife():
    name = 'KNIFE'
    str_desc = 'A simple KNIFE.'
    dmg_low = 10
    dmg_high = 30
    return create_weapon(name, str_desc, dmg_low, dmg_high)


def create_slingshot():
    name = 'SLINGSHOT'
    str_desc = 'A simple SLINGSHOT that can be used to fire small rocks.'
    dmg_low = 20
    dmg_high = 50
    return create_weapon(name, str_desc, dmg_low, dmg_high)


def create_axe():
    name = 'AXE'
    str_desc = 'A crudely made stone AXE.'
    dmg_low = 40
    dmg_high = 100
    return create_weapon(name, str_desc, dmg_low, dmg_high)


def create_bow():
    name = 'BOW'
    str_desc = 'A wooden BOW with plenty of arrows.'
    dmg_low = 50
    dmg_high = 100
    return create_weapon(name, str_desc, dmg_low, dmg_high)


def create_gun():
    name = 'GUN'
    str_desc = 'A strange alien GUN that fires high-energy blasts.'
    dmg_low = 90
    dmg_high = 100
    return create_weapon(name, str_desc, dmg_low, dmg_high)


class Consumable(Item):
    """Consumable class in game."""
    def __init__(self, name, str_desc, value, health_gain, use_count):
        """Creates a consumable object.\n
        parameters: name, str_desc, value, use_count"""
        self._name = name
        self._str_desc = str_desc
        self._type = "CONSUMABLE"
        self._value = value
        self._health_gain = health_gain
        self._use_count = use_count

    def __str__(self):
        return self._name + ": " + self._str_desc + " value: " + str(self._value) + ", use count:" + str(self._use_count) 
        
    def get_value(self):
        """get the value of the consumable."""
        return self._value
    
    def get_use_count(self):
        """get the remaining use count"""
        return self._use_count

    def get_health_gein(self):
        return self._health_gain

    # EDIT: this method should probably pass in a unit argument to change it
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


def create_consumable(name, str_desc, value, use_count):
    return Consumable(name, str_desc, value, use_count)


def create_medkit(quantity):
    name = 'MEDKIT'
    str_desc = 'A simple MEDKIT. Restores 50 health when used.'
    value = 100
    health_gain = 50
    use_count = quantity
    return create_consumable(name, str_desc, value, health_gain, use_count)


def create_berries(quantity):
    name = 'BERRIES'
    str_desc = 'A bundle of alien BERRIES. Restores 10 health when used.'
    value = 20
    health_gain = 10
    use_count = quantity
    return create_consumable(name, str_desc, value, health_gain, use_count)


def create_rations(quantity):
    name = 'RATIONS'
    str_desc = 'A pack of emergency RATIONS. Restores 20 health when used.'
    value = 30
    health_gain = 20
    use_count = quantity
    return create_consumable(name, str_desc, value, health_gain, use_count)


def create_vitamins(quantity):
    name = 'VITAMINS'
    str_desc = 'A small bottle of VITAMINS. Restores 30 health when used.'
    value = 30
    health_gain = 30
    use_count = quantity
    return create_consumable(name, str_desc, value, health_gain, use_count)


def create_meat(quantity):
    name = 'MEAT'
    str_desc = 'The MEAT of an alien creature. Restores 15 health when used.'
    value = 10
    health_gain = 15
    use_count = quantity
    return create_consumable(name, str_desc, value, health_gain, use_count)
