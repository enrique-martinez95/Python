#  File: LinearEquations.py
#  Description: a program which creates, prints and performs operations on linear
#  equations
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 4/6/20
#  Date Last Modified: 4/9/20
#  Note: Apologies for the late submission, I've been playing catch up since
#  before spring break and am just getting around to understanding the material

class LinearEquation:

    def __init__(self,m,b):

        self.m = m
        self.b = b

    def showEq(self):

        equate = ''
        if self.m != 0:
            if self.m < 0:
                equate = "- "+str(-1*self.m)+"x"

            else:
                equate = str(self.m)+"x"

            if self.b != 0:
                if self.b < 0:
                    if len(equate) > 0:
                        equate = equate + " + " + str(self.b)

                    else:
                        equate = str(self.b)
        return equate

    def add(self,other):

        return LinearEquation(self.m + other.m,self.b+other.b)

    def sub(self, other):
        return LinearEquation(self.m-other.m, self.b-other.b)

    def compose(self, other):
        return LinearEquation(self.m*other.m, self.m*other.b+self.b)

    def evaluate(self,val):
        return(self.m*val+self.b)

def main():

    f = LinearEquation(5,3)
    print("f(x) =", f.showEq(),"+ 3")
    print("f(3) =", f.evaluate(3),"\n")

    g = LinearEquation(-2,-6)
    print("g(x) =",g.showEq())
    print("g(-2) =",g.evaluate(-2),"\n")

    h = f.add(g)
    print("h(x) = f(x) + g(x) =",h.showEq())
    print("h(-4) =", h.evaluate(-4),"\n")

    j = f.sub(g)
    print("j(x) = f(x) -g(x) =",j.showEq())
    print("j(-4) =", j.evaluate(-4),"\n")

    k = f.compose(g)
    print("f(g(x)) =", k.showEq(), "\n")

    m = g.compose(f)
    print("g(f(x)) =",m.showEq(), "\n")

    g = LinearEquation(5,-3)
    print("g(x) =",g.showEq())
    print("g(-2) =", g.evaluate(-2), "\n")

    h = f.add(g)
    print("h(x) = f(x) + g(x) =", h.showEq())
    print("h(-4) =",h.evaluate(-4), "\n")

    j = f.sub(g)
    print("j(x) = f(x) - g(x) =", j.showEq())
    print("j(-4) =", j.evaluate(-4), "\n")

main()
    
