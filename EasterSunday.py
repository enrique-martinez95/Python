##File: EasterSunday.py
##Description: a file that asks the user for a year
##and returns the day Easter Sunday falls on that year.
##Student's name: Enrique Martinez
##Student's EID: egm657
##Course Name: CS 303 E
##Unique Number: 50191
##
##Date created: 2/3/2020
##Date last modified: 2/3/2020
def main():
    

##Ask the user for the year (such as 2001). Save the year in y.
    y = int(input("Enter year:"))
    year = y
##Divide y by 19 and call the remainder a. Ignore the quotient.
    a = y%19
##Divide y by 100 to get a quotient b and a remainder c.
    b = y//100
    c = y%100
##Divide b by 4 to get a quotient d and a remainder e.
    e = b%4
    d = b//4
##Divide 8 * b + 13 by 25 to get a quotient g. Ignore the remainder.
    g = (8*b+13)//25
##Divide 19 * a + b - d - g + 15 by 30 to get a remainder h. Ignore the quotient.
    h = (19*a+b-d-g+15)%30  
##Divide c by 4 to get a quotient j and a remainder k.
    k = c%4
    j = c//4
##Divide a + 11 * h by 319 to get a quotient m. Ignore the remainder.
    m = (a+11*h)//319
##Divide 2 * e + 2 * j - k - h + m + 32 by 7 to get a remainder r. Ignore the quotient.
    r = (2*e+2*j-k-h+m+32)%7    
##Divide h - m + r + 90 by 25 to get a quotient n. Ignore the remainder.
    n = (h-m+r+90)//25
##Divide h - m + r + n + 19 by 32 to get a remainder p. Ignore the quotient.
    p = (h-m+r+n+19)%32

    print("In",year,"Easter Sunday is on month",int(n),"and day",int(p))
main()
