#  File: MagicSquares.py
#  Description: A file which prints odd numbers magic squares
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 4/23/2020
#  Date Last Modified: 4/23/2020

# create the class for the magic squares

class MagicSquare:
    def __init__(self, side):
        self.sideLength = side
        self.grid = [[0 for x in range(side)] for x in range(side)]
        self.pop()

#populate the square with numbers according to algorithm
        
    def pop(self):
        
        i = 1
        a = 0
        b = int(self.sideLength/2)
        
        while(True):
            self.grid[a][b]=i
            if i== self.sideLength**2:
                break
            if i % self.sideLength == 0:
                a = (a+1) % self.sideLength
            else:
                a = (a - 1 + self.sideLength) % self.sideLength
                b = (b+1) % self.sideLength
            i += 1
  
    def display(self):
        for x in self.grid:
            print(' '.join('{:>5}'.format(y) for y in x))

#call the methods in the main program

def main():
    

    for side in range(1,14,2):
        print("Magic Square of size ", side )
        print()
        ms = MagicSquare(side)
        ms.display()
        print()

main()
