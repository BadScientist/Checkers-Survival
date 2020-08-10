from NPCs import *
from events import gen_event

# TODO: Room descriptions (short description) needs the landscape description

# select from random list of landscapes


class Room: 
    
    def __init__(self, level_num, long_desc='You are in Standard Room',
                 shrt_desc='Standard'):
        """
        Creates a Room object that can be added to the level map.
        :param x: room's position (y axis), to prevent overlaps between rooms
        :param y: room's position (y axis), to prevent overlaps between rooms
        :param long_desc: string displayed by here command
        :param shrt_desc: string displayed by look command
        :param N: adjacent Room object to the north
        :param S: adjacent Room object to the south
        :param E: adjacent Room object to the east
        :param W: adjacent Room object to the west
        :param seen: if Room has been looked at or entered (T/F). If T, Room's
                     contents e.g. animal can be seen. Otherwise '?' appears
        :param character: Character object located in Room
        :param animal: Animal object located in Room
        :param item: Item object located in Room
        :param next_level: If True, allows user to progress to next level
        """
        self.x = 0
        self.y = 0
        self.long_desc = long_desc
        self.shrt_desc = shrt_desc
        self.N = None
        self.S = None
        self.E = None
        self.W = None
        self.seen = False
        self.character = gen_character(level_num)
        self.animal = gen_animal(level_num)
        self.item = gen_item(level_num)
        self.next_level = False
        self.event = gen_event()
    
    def apply_position(self, x, y):
        self.x = x
        self.y = y
    
    def apply_long(self, long_desc):
        # change the long description of the room. Supply a string as parameter
        self.long_desc = long_desc
    
    def apply_shrt(self, shrt_desc):
        # change the short description of the room. Supply a string as parameter
        self.shrt_desc = shrt_desc
        
    def apply_path(self, direction, target):
        # Creates a path between one room and another e.g from room1 to room2.
        # If self is room1, and direction is 'N' i.e North, then the N variable
        # of room1 is set to room2.
        
        # Note however, that none of the variables in room2 are changed.
        # The create_path() function below (outside class defn) rectifies this.
        
        # To be successful, it checks if the path/direction is already occupied
        #   and if there's an existing path to target i.e you don't want 'N'
        #   'W' to point to room2 - doesn't make sense.
        # Also, to prevent overlaps, it ensures no other room is at same
        # position

        if self != target:
            if self.get_adjacent_room(direction) is None:
                all_paths = ['N', 'S', 'E', 'W']
                for path in all_paths:
                    if getattr(self, path) == target:
                        return False           # failure
                setattr(self, direction, target)
                return True
            else:
                return False
        else:
            return False
    
    def apply_seen(self, state=True):
        # default is True because this will mostly be called to set seen to T
        self.seen = state
        
    def apply_next_level(self, state=True):
        self.next_level = state
    
    def get_position(self):
        return [self.x, self.y]
    
    def get_long_desc(self):
        # returns the long description of the room
        # Print current room's long description
        
        desc = self.long_desc + '\n'
        # If present, print character's description
        if self.character is not None:
            desc += self.character.get_description() + '\n'
        # If present, print animal's description.
        if self.animal is not None:
            desc += self.animal.get_description() + '\n'
        # If present, print item's name.
        if self.item is not None:
            item_name = self.item.get_name()
            desc += "You spot "
            if item_name[-1] == 'S':
                desc += "some "
            else:
                desc += "a "
            desc += item_name + ".\n"
        
        # get seen rooms' short descriptions
        for path in self.get_existing_paths():
            adj_room = self.get_adjacent_room(path)
            if adj_room is not None:
                if adj_room.get_seen():
                    desc += 'To the ' + path + ' you see '
                    desc += adj_room.get_shrt_desc() + '\n'
        return desc
 
    def get_shrt_desc(self):
        # returns the short description of the room
        return self.shrt_desc

    def get_character(self):
        return self.character

    def get_animal(self):
        return self.animal

    def remove_animal(self):
        self.animal = None
        
    def get_item(self):
        return self.item

    def remove_item(self):
        self.item = None

    def get_event(self):
        return self.event

    def remove_event(self):
        self.event = None
    
    def get_adjacent_room(self, direction):
        # pass direction eg 'N' ie North, and it returns the room N of self. If
        # there's no room to the N, then it returns None (the default value)
        return getattr(self, direction)
    
    def get_next_level(self):
        return self.next_level
    
    def get_existing_paths(self):  # used for level display
        # returns an array with all paths/directions that have an assigned room
        all_paths = ['N','S','E','W']
        idx = 0
        while idx < len(all_paths):
            direction = all_paths[idx]
            if getattr(self, direction) is None:
                all_paths.remove(direction)
                idx -= 1
            idx += 1
        return all_paths
    
    def get_empty_paths(self):  # used for level generation
        # returns an array with all paths/directions without an assigned room
        all_paths = ['N','S','E','W']
        idx = 0
        while idx < len(all_paths):
            direction = all_paths[idx]
            if getattr(self, direction) is not None:
                all_paths.remove(direction)
                idx -= 1
            idx += 1
        return all_paths
    
    def get_seen(self):
        return self.seen

    # Functions to generate a random level with supplied no. of rooms

# Concept:
#   We supply the no. of rooms to create in the level e.g 10
#   Each room is created one by one and randomly joined to one of the existing
#       rooms i.e the existing 'bunch' (I use that term in comments below).
#
#   so after creating first two rooms (which are obviously joined together)
#   we randomise which of the two rooms the third will be joined to, as well as
#   the direction it will be joined to the third.
#   AND SO FORTH according to the no. of rooms we want.
#
#
# Way Of Preventing Errors and Maintaining Efficiency:
#   Even though the array all_rooms[] has all the rooms, its from avail_rooms[]
#        that the room the new room will be joined to is selected
#   avail_rooms[] elements are the indexes of rooms in all_rooms[] which have
#       unused paths (i.e a room can be joined to them)
#
#   In the event that a room is found to have all paths filled, the operation
#       of joining the room fails but is repeated. However, first the index of
#       that room is removed from avail_room[] such that it cant be selected


def create_path(parent, target, paths):
    # Function is necessary so that when a path between room1 and room2 is
    # created e.g. to the North of room1, the south of room2 will point to
    # room1
    
    # Arguments:
    #   parent is the existing room the new room (target) will be joined to
    
    # only possible reason for failure (False) is the parent's paths are filled
    opposite_dir = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }
    if paths:
        idx = randint(0, len(paths) - 1)  # randomise direction
        direction = paths[idx]
        
        position = parent.get_position()
        if direction == 'N':
            target.apply_position(position[0], position[1]+1)
        elif direction == 'S':
            target.apply_position(position[0], position[1]-1)
        elif direction == 'E':
            target.apply_position(position[0]+1, position[1])
        elif direction == 'W':
            target.apply_position(position[0]-1, position[1])
            
        if parent.apply_path(direction, target) is False:
            return False
        else:
            return target.apply_path(opposite_dir[direction], parent)
    else:
        return False


def gen_random_level(room_num, level_num):
    # see Concept above for better understanding of function
    all_rooms = []
    avail_rooms = []  # has index of rooms with an available path
    for i in range(0, room_num):
        all_rooms.append(Room(level_num))  # create the new room (target)
        avail_rooms.append(i)
        if i == 0:
            continue
        flag = False
        while flag is False:
            idx = 0
            if i == 1:  # 2 rooms only
                parent = all_rooms[0]
            if i > 1:  # more than 2 rooms
                idx = randint(0,len(avail_rooms)-2)
                parent = all_rooms[avail_rooms[idx]]
            avail_paths = parent.get_empty_paths()  # parent's available paths
            flag = create_path(parent, all_rooms[i], avail_paths)
            if flag is False:
                if idx in avail_rooms:       # remove room from
                    avail_rooms.remove(idx)  # 'bunch'-paths filled
    #choose room with 'next_level' event allowing user to progress to nxt lvl
    all_rooms[randint(0, room_num-1)].apply_next_level(True)
    return all_rooms
