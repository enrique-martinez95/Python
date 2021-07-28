#  File: Project1.py
#  Description: A program in which a user moves about a floorplan
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 4/20/2020
#  Date Last Modified: 4/23/2020

class Room:

    def __init__(self,name,north,east,south,west,up,down):
        # add your code here
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down

    def displayRoom(self):
        print("Room name:\t" + self.name)
        if (self.north is not None):
            print("\tRoom to the north:\t" + self.north)
        if (self.east is not None):
            print("\tRoom to the east:\t" + self.east)
        if (self.south is not None):
            print("\tRoom to the south:\t" + self.south)
        if (self.west is not None):
            print("\tRoom to the west:\t" + self.west)
        if (self.up is not None):
            print("\tRoom above:\t\t" + self.up)
        if (self.down is not None):
            print("\tRoom below:\t\t" + self.down)
        print()
        

def createRoom(roomData):
        # add your code here
        return Room(roomData[0], roomData[1], roomData[2], roomData[3], roomData[4], roomData[5], roomData[6])

def look():
        # add your code here
        print("You are currently in the " + current.name + ".")

def getRoom(name):
        # add your code here
        for room in floorPlan:
            if (room.name == name):
                return room
        return None
        
def move(direction):
        # add your code here
        if (direction == "north"):
            if (current.north is not None):
                print("You are now in the " + current.north + ".")
                return getRoom(current.north)
        if (direction == "east"):
            if (current.east is not None):
                print("You are now in the " + current.east + ".")
                return getRoom(current.east)
        if (direction == "south"):
            if (current.south is not None):
                print("You are now in the " + current.south + ".")
                return getRoom(current.south)
        if (direction == "west"):
            if (current.west is not None):
                print("You are now in the " + current.west + ".")
                return getRoom(current.west)
        if (direction == "up"):
            if (current.up is not None):
                print("You are now in the " + current.up + ".")
                return getRoom(current.up)
        if (direction == "down"):
            if (current.down is not None):
                print("You are now in the " + current.down + ".")
                return getRoom(current.down)

        print("You can't move in that direction.")
        return current

def displayAllRooms():
        # add your code here
        for room in floorPlan:
            room.displayRoom()

##########################################################################
###     All code below this is given to you.  DO NOT EDIT IT unless    ###
###     you need to adjust the indentation to match the indentation    ###
###     of the rest of your code.                                      ###
##########################################################################
        
def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable
    
    room1 = ["Living Room","Dining Room",None,None,None,"Upper Hall",None]
    room2 = ["Dining Room",None,None,"Living Room","Kitchen",None,None]
    room3 = ["Kitchen",None,"Dining Room",None,None,None,None]
    room4 = ["Upper Hall","Bathroom","Small Bedroom","Master Bedroom",None,None,"Living Room"]
    room5 = ["Bathroom",None,None,"Upper Hall",None,None,None]
    room6 = ["Small Bedroom",None,None,None,"Upper Hall",None,None]
    room7 = ["Master Bedroom","Upper Hall",None,None,None,None,None]

    floorPlan = [createRoom(room1),createRoom(room2),createRoom(room3),createRoom(room4),createRoom(room5),createRoom(room6),createRoom(room7)]

def main():

    global current      # make the variable "current" a global variable
    
    loadMap()
    
    displayAllRooms()

    # TEST CODE:  walk around the house
    
    current = floorPlan[0]      # start in the living room
    look()                      # Living Room
    
    current = move("south")     # can't move this direction
    current = move("west")      # can't move this direction
    current = move("north")     # Dining Room
    current = move("south")     # Living Room
    current = move("up")        # Upper Hall
    look()                      # Upper Hall
    current = move("east")      # Small Bedroom
    current = move("east")      # can't move this direction
    current = move("west")      # Upper Hall
    current = move("south")     # Master Bedroom
    current = move("north")     # Upper Hall
    current = move("north")     # Bathroom
    current = move("south")     # Upper Hall
    look()                      # Upper Hall
    current = move("west")      # can't move this direction
    look()                      # still in the Upper Hall
    current = move("down")      # Living Room
    current = move("north")     # Dining Room
    current = move("west")      # Kitchen
    current = move("north")     # can't move this direction

main()
