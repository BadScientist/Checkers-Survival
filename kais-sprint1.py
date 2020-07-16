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
        
