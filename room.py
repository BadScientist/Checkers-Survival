import random
import tkinter as tk

random.seed()

class Room: 
    #Variables:
    #   long_desc -> printed in-game when within the room
    #   shrt_desc -> printed in-game when in a room adjacent to this room
    #   N,S,E,W   -> point to adjacent room in respective direction (in 2D)
    #                set to None (null) if not yet defined
    
    #Functions:
    #   all variables in the class can be obtained and/or changed with the
    #   functions below. A short explanation of each function is provided.
    
    #Example of Room Class Use:
    #   print(room_1.get_long_desc())
    #   print(room_1.get_shrt_desc())
    #   room_1.apply_long('goin don know')
    #   room_1.apply_path('N', room_2)
    #   print(room_1.__dict__) to print all class vars
    
    def __init__(self, long_desc='Standard Room', shrt_desc='Standard', N=None,
                 S=None, E=None, W=None):
        self.long_desc = long_desc
        self.shrt_desc = shrt_desc
        self.N = N
        self.S = S
        self.E = E
        self.W = W
    
    def apply_long(self, long_desc):
        #change the long description of the room. Supply a string as parameter
        self.long_desc = long_desc
    
    def apply_shrt(self, shrt_desc):
        #change the short description of the room. Supply a string as parameter
        self.shrt_desc = shrt_desc
        
    def apply_path(self, direction, target):
        #Creates a path between one room and another e.g from room1 to room2.
        #If self is room1, and direction is 'N' i.e North, then the N variable
        #of room1 is set to room2.
        
        #Note however, that none of the variables in room2 are changed.
        #The create_path() function below (outside class defn) rectifies this.
        
        #To be successful, it checks if the path/direction is already occupied
        #and if there's an existing path to target i.e you don't want 'N'
        #'W' to point to room2 - doesn't make sense.
        if self != target:
            if self.get_adjacent_room(direction) == None:
                all_paths = ['N','S','E','W']
                for path in all_paths:
                    if getattr(self, path) == target:
                        return False           #failure
                setattr(self, direction, target)
                return True
            else:
                return False
        else:
            return False
    
    def get_long_desc(self):
        #returns the long description of the room
        return self.long_desc
 
    def get_shrt_desc(self):
        #returns the short description of the room
        return self.shrt_desc
    
    def get_adjacent_room(self, direction):
        #pass direction eg 'N' ie North, and it returns the room N of self. If
        #there's no room to the N, then it returns None (the default value)
        return getattr(self, direction)
    
    def get_existing_paths(self): #used for level display
        #returns an array with all paths/directions that have an assigned room
        all_paths = ['N','S','E','W']
        idx = 0
        while idx < len(all_paths):
            direction = all_paths[idx]
            if getattr(self, direction) == None:
                all_paths.remove(direction)
                idx-=1
            idx+=1
        return all_paths
    
    def get_empty_paths(self): #used for level generation
        #returns an array with all paths/directions without an assigned room
        all_paths = ['N','S','E','W']
        idx = 0
        while idx < len(all_paths):
            direction = all_paths[idx]
            if getattr(self, direction) != None:
                all_paths.remove(direction)
                idx-=1
            idx+=1
        return all_paths


    #Functions to generate a random level with supplied no. of rooms

#Concept:
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
#Way Of Preventing Errors and Maintaining Efficiency:
#   Even though the array all_rooms[] has all the rooms, its from avail_rooms[]
#        that the room the new room will be joined to is selected
#   avail_rooms[] elements are the indexes of rooms in all_rooms[] which have
#       unused paths (i.e a room can be joined to them)
#
#   In the event that a room is found to have all paths filled, the operation
#       of joining the room fails but is repeated. However, first the index of
#       that room is removed from avail_room[] such that it cant be selected

def create_path(parent, target, paths):
    #Function is necessary so that when a path between room1 and room2 is
    #created e.g. to the North of room1, the south of room2 will point to
    #room1
    
    #Arguments:
    #   parent is the existing room the new room (target) will be joined to
    
    #only possible reason for failure (False) is the parent's paths are filled
    opposite_dir = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }
    if paths:
        idx = random.randint(0,len(paths)-1) #randomise direction
        direction = paths[idx]
        if parent.apply_path(direction, target) is False:
            return False
        else:
            return target.apply_path(opposite_dir[direction], parent)
    else:
        return False

def gen_random_level(room_num):
    #see Concept above for better understanding of function
    
    all_rooms = []
    avail_rooms = [] #has index of rooms with an available path
    for i in range(0, room_num):
        all_rooms.append(Room()) #create the new room (target)
        avail_rooms.append(i)
        if i == 0:
            continue
        flag = False
        while flag == False:
            if i == 1: #2 rooms only
                parent = all_rooms[0]
                avail_paths = parent.get_empty_paths()#parent's available paths
                flag = create_path(parent, all_rooms[i], avail_paths)
            if i > 1:  #more than 2 rooms
                idx = random.randint(0,len(avail_rooms)-2)
                parent = all_rooms[avail_rooms[idx]]
                avail_paths = parent.get_empty_paths()#parent's available paths
                flag = create_path(parent, all_rooms[i], avail_paths)
            if flag == False:
                avail_rooms.remove(idx) #remove room from 'bunch'-paths filled
    #for i in range(0, room_num):
        #print(all_rooms[i])
        #print(all_rooms[i].__dict__)
        #print('')
    #print(avail_rooms)
    return all_rooms

#Level generation functions complete



level = gen_random_level(10)


                            #GUI Map Definition

#root = tk.Tk(className=" Map")
#root.geometry("840x540")

#vert_scroll = tk.Scrollbar(root, orient='vertical')
#vert_scroll.pack(side='right', fill='y')
#hori_scroll = tk.Scrollbar(root, orient='horizontal')
#hori_scroll.pack(side='bottom', fill='x')

def locate_pivot(level):
    #pivot is the room which is most centrally located in the map
    prospects = []
    flag = False
    i = 0
    while flag == False:
        flag = False
        for room in level:
            if len(room.get_empty_paths()) == i:
                prospects.append(room)
                flag = True
        if flag == False:
            i+=1
        if i == 5: #just 1 room in the level
            return room
    pivot = prospects[0]
    highest_pts = 0
    for room in prospects:
        pts = 0
        paths = room.get_existing_paths()
        for path in paths:
            if room.get_adjacent_room(path) in prospects:
                pts+=1
        if pts > highest_pts:
            highest_pts = pts
            pivot = room
    return pivot

def display_path(canvas, direction, x, y):
    #direction is the direction of the line representing a path
    #x and y are mark the centre of the room shape
    if direction == 'N':
        canvas.create_line(x, y-21, x, y-39) #Up
    elif direction == 'S':
        canvas.create_line(x, y+21, x, y+39) #Down
    elif direction == 'E':
        canvas.create_line(x+21, y, x+39, y) #Right
    elif direction == 'W':
        canvas.create_line(x-21, y, x-39, y) #Left

def display_level(canvas, room, x, y):
    #room is the current room being examined to be printed
    #x and y are mark the centre of the room shape
    return

def start_level_IO(level):
    pivot = locate_pivot(level)
    #canvas = tk.Canvas(root, width=800, height=500)
    x = 405 #centre of the screen on x-axis
    y = 235 #centre of the screen on y-axis
    #display_level(canvas, pivot, x, y)
    #canvas.pack()

#coordinates: X-start, Y-start, X-end, Y-end
#each room takes maximum of 80x80

#maximise the canvas according to the number of rooms
#canvas = tk.Canvas(root, width=800, height=500)
#x = 405 #centre of the screen on x-axis
#y = 235 #centre of the screen on y-axis

#Templates
#canvas.create_rectangle(x-20, y-20, x+20, y+20, outline="#fb0", fill="#fb0")
#canvas.create_line(x+21, y, x+39, y) #Right
#canvas.create_line(x, y+21, x, y+39) #Down
#canvas.create_line(x-21, y, x-39, y) #Left
#canvas.create_line(x, y-21, x, y-39) #Up
#canvas.pack()

#returnButton = tk.Button(root, text="OK", padx=50, command=root.destroy)
#returnButton.pack()

#root.mainloop()