#  File: NextDay.py
#  Description: A program that asks the user for a date and returns the next day
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 2/17/2020
#  Date Last Modified: 2/18/2020

def main():
    
    nextYear = int(input("Please enter the year:"))
    nextMonth = raw_input("Please enter the month:")
    nextDay = int(input("Please enter the day:"))
  
    leapYear = (nextYear % 4 == 0 and nextYear % 100 != 0) or (nextYear % 400 == 0)
main()
