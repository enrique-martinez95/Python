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
  
# Asks user for a date
  
    nextYear = int(input("Please enter the year:"))
    nextMonth = raw_input("Please enter the month:")
    nextDay = int(input("Please enter the day:"))
  
    leapYear = (nextYear % 4 == 0 and nextYear % 100 != 0) or (nextYear % 400 == 0)
    if (nextMonth == "January" and nextDay == 31):
        nextMonth = "February"
        nextDay = 1
  
  # Determines if the year is a leap year
    elif nextMonth == "February" and nextDay == 28 and leapYear == True:
        nextDay = 29
  
    elif nextMonth == "February" and nextDay == 28 and leapYear == False:
      nextMonth = "March"
      nextDay = 1
  
    elif nextMonth == "February" and nextDay == 29:
      nextMonth = "March"
      nextDay = 1
  
  # Else determines the next day
  
    elif nextMonth == "March" and nextDay == 31:
      nextMonth = "April"
      nextDay = 1
  
    elif nextMonth == "April" and nextDay == 30:
      nextMonth = "May"
      nextDay = 1
  
    elif nextMonth == "May" and nextDay == 31:
      nextMonth = "June"
      nextDay = 1
  
    elif nextMonth == "June" and nextDay == 30:
      nextMonth = "July"
      nextDay = 1
  
    elif nextMonth == "July" and nextDay == 31:
      nextMonth = "August"
      nextDay = 1
  
    elif nextMonth == "August" and nextDay == 31:
      nextMonth = "September"
      nextDay = 1
  
    elif nextMonth == "September" and nextDay == 30:
      nextMonth = "October"
      nextDay = 1
  
    elif nextMonth == "October" and nextDay == 31:
      nextMonth = "November"
      nextDay = 1
  
    elif nextMonth == "November" and nextDay == 30:
      nextMonth = "December"
      nextDay = 1
  
    elif nextMonth == "December" and nextDay == 31:
      nextMonth = "January"
      nextDay = 1
      nextYear = nextYear+1
  
    else:
      nextDay = nextDay+1
    print("The next day is "+ nextMonth + " " +str(nextDay)+ ", "+str(nextYear)+ ".")
  
main()
