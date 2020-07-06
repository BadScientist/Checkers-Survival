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
        setattr(self, direction, target)
    
    def get_long_desc(self):
        return self.long_desc
 
    def get_shrt_desc(self):
        return self.shrt_desc
    
    def get_adjacent_room(self, direction):
    #direction eg N, S ...;
        return getattr(self, direction)

#room_1 = Room('haha', 'lool')
#room_2 = Room()

#print(room_1.get_long_desc())
#print(room_1.get_shrt_desc())

#room_1.apply_long('goin don know')
#room_1.apply_path('N', room_2)

#print(room_1.__dict__)
#to print all class vars