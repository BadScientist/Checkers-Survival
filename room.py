#example use of functions below class definition

class Room:
    
    #Variables:
    #   long_desc -> printed in-game when within the room
    #   shrt_desc -> printed in-game when in a room adjacent to this room
    #   N,S,E,W   -> point to adjacent room in respective direction (in 2D)
    #                set to None (null) if not yet defined
    
    def __init__(self, long_desc=None, shrt_desc=None, N=None, S=None, E=None, 
                 W=None):
        self.long_desc = long_desc
        self.shrt_desc = shrt_desc
        self.N = N
        self.S = S
        self.E = E
        self.W = W
    
    def apply_long(self, long_desc):
        self.long_desc = long_desc
    
    def apply_shrt(self, shrt_desc):
        self.shrt_desc = shrt_desc
        
    def apply_path(self, direction, target):
    #direction eg N, S ...; target is the room path leads to
        #check if path already occupied and if there's existing path to target
        if self.get_adjacent_room(direction) == None:
            all_paths = ['N','S','E','W']
            for path in all_paths:
                if getattr(self, path) == target:
                    return
            setattr(self, direction, target)
        #***************maybe throw error if occupied****************
    
    def get_long_desc(self):
        return self.long_desc
 
    def get_shrt_desc(self):
        return self.shrt_desc
    
    def get_adjacent_room(self, direction):
    #direction eg N, S ...;
        return getattr(self, direction)
    
    def get_empty_paths(self): #used for level generation
    #get all paths/directions that don't have an assigned room
    #returns an array of all available paths
        all_paths = ['N','S','E','W']
        idx = 0
        while idx < len(all_paths):
            direction = all_paths[idx]
            if getattr(self, direction) != None:
                all_paths.remove(direction)
                idx-=1
            idx+=1
        return all_paths


def gen_random_level(room_num):
    rooms = []
    for i in range(0, room_num):
        rooms.append(Room())
    print(rooms)
    

room_1 = Room('haha', 'lool')
room_2 = Room()
room_3 = Room()

gen_random_level(3)

#print(room_1.get_long_desc())
#print(room_1.get_shrt_desc())

#room_1.apply_long('goin don know')
#room_1.apply_path('N', room_2)

#print(room_1.__dict__)
#to print all class vars