#  File: Project2.py
#  Description: An expansion of project 1, a game in which a user moves
#  throughout a house with various items
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 4/28/2020
#  Date Last Modified: 5/7/2020

class Room:

    def __init__(self,contents):
        # add your code here
        self.contents = contents
        self.name = self.contents[0]
        self.north = self.contents[1]
        self.east = self.contents[2]
        self.south = self.contents[3]
        self.west = self.contents[4]
        self.up = self.contents[5]
        self.down = self.contents[6]
        self.items = []
        for i in range(7, len(self.contents)):
            self.items.append(self.contents[i])

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
        print("\tRoom contents:\t\t" + str(self.items))
        print()
        

def createRoom(roomData):
        # add your code here
        newData = []
        roomData = roomData.split(",")
        for data in roomData:
            if (data == "None"):
                newData.append(None)
            else:
                newData.append(data.strip('"'))
        return Room(newData)

def look():
        # add your code here
        print("You are currently in the " + current.name + ".")
        print("Contents of the room:")
        if (len(current.items) == 0):
            print("\tNone")
        else:
            for item in current.items:
                print("\t" + item)
        # print()

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
    floorPlan = []

    f = open("ProjectData.txt")
    data = f.readlines()
    for line in data:
        line = line.strip()
        floorPlan.append(createRoom(line))


def pickup(item):

    found = False
    for i in range(len(current.items)):
        if (current.items[i] == item):
            found = True
            print("You now have the",item + ".")
            inventory.append(item)
            del current.items[i]
            break
    if (found == False):
        print("That item is not in this room.")

def drop(item):
    found = False
    for i in range(len(inventory)):
        if (inventory[i] == item):
            found = True
            print("You have dropped the", item + ".")
            current.items.append(inventory[i])
            del inventory[i]
            break

    if (found == False):
        print("You don't have that item.")

def listInventory():
    print("You are currently carrying:")
    if (len(inventory) == 0):
        print("\tnothing.")
    else:
        for item in inventory:
            print("\t" + item)

def printHelp():
    print("look:        display the name of the current room and its contents")
    print("north:       move north")
    print("east:        move east")
    print("south:       move south")
    print("west:        move west")
    print("up:          move up")
    print("down:        move down")
    print("inventory:   list what items you're currently carrying")
    print("get <item>:  pick up an item currently in the room")
    print("drop <item>: drop an item you're currently carrying")
    print("help:        print this list")
    print("exit:        quit the game")


def main():

    global current      # make the variable "current" a global variable
    global inventory
    inventory = []
    loadMap()
    
    displayAllRooms()
    print("-"*10,"\n")

    # TEST CODE:  walk around the house
    userInput = "look"
    current = floorPlan[0]      # start in the living room
    
    splitted = []
    while (True):
        splitted = userInput.split(' ')
        if (userInput == "look"):
            look()
        elif (userInput == "north"):
            current = move("north")
        elif (userInput == "east"):
            current = move("east")
        elif (userInput == "south"):
            current = move("south")
        elif (userInput == "west"):
            current = move("west")
        elif (userInput == "help"):
            printHelp()
        elif (userInput == "inventory"):
            listInventory()
        elif (splitted[0] == "get"):
            pickup(splitted[1])
        elif (splitted[0] == "drop"):
            drop(splitted[1])
        elif (userInput == "exit"):
            print("Quitting the game.")
            break
        else:
            print("Invalid input. Enter 'help' to see the available commands.")

        print()
        userInput = input("Enter a command: ")


main()
