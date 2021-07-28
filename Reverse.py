##File: Reverse.py
##Description: a file that asks the user for a number
##and returns the number in reverse order.
##Student's name: Enrique Martinez
##Student's EID: egm657
##Course Name: CS 303 E
##Unique Number: 50191
##
##Date created: 2/8/2020
##Date last modified: 2/8/2020

def main():

    #The user inputs a 4 digit number
    number = int(input("Enter an integer:"))

    #To get the first (last) digit, we divide by 10 and save the remainder
    #we must also divide the input by 10 to get the remaining digits
    first = number%10
    number = number//10

    #Repeat for remaining digits

    second = number%10
    number = number//10

    third = number%10
    number = number//10

    #print the reversed number
    #note: strings are used so the program doesn't simply add the numbers
    print("The reversed number is: "+str(first)+str(second)+str(third)+str(number)+".")

main()
