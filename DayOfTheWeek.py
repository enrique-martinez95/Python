#  File: DayOfTheWeek.py
#  Description: A program that asks the user for a date and returns the day
#  of the week the day falls on.
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 2/23/2020
#  Date Last Modified: 2/23/2020

def main():

#   Ask the user for a date in year, month, day format

    year = int(input("Please enter the year (an integer): "))
    
    month = input("Please enter the month (a string): ")
    
    day = int(input("Please enter the day (an integer): "))

#   calculate value for a given the month

    if month == "January":
        a = 11
    elif month =="February":
        a=12
    elif month =="March":
        a = 1
    elif month == "April":
        a= 2
    elif month == "May":
        a = 3
    elif month =="June":
        a = 4
    elif month == "July":
        a = 5
    elif month == "August":
        a = 6
    elif month == "September":
        a = 7
    elif month == "October":
        a = 8
    elif month == "November":
        a = 9
    else:
        a = 10

#   assign value for b

    b = day

#   calculate the value for c and d

    if a == 11 or a == 12:
        year = year-1

    if year <= 1999:
        c= year % 1900
        d = 19

    elif year <= 2099:
        c = year % 2000
        d = 20
    else:
        c = 0
        d = 21

#   Zeller's Congruence

    w = (13 * a - 1) // 5
    x =  c//4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z%7
    r = (r+7) % 7

    if r == 0:
        dotw = "Sunday"
    elif r == 1:
        dotw = "Monday"
    elif r == 2:
        dotw = "Tuesday"
    elif r == 3:
        dotw = "Wednesday"
    elif r == 4:
        dotw = "Thursday"
    elif r == 5:
        dotw = "Friday"
    else:
        dotw = "Saturday"
        
#   print the day of the week

    print("The day of the week is " + dotw +".")


main()
