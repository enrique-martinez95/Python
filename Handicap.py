#  File: Handicap.py
#  Description: A program that calculates a bowler's average score from 3 games
#  and their handicap.
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created:2/4/2020
#  Date Last Modified:2/4/2020
def main():
    #Ask the user to input scores for 3 games
    
    g1 = int(input("Enter Game 1:"))
    g2 = int(input("Enter Game 2:"))
    g3 = int(input("Enter Game 3:"))

    #calculate the average score of the games.

    average = int((g1+g2+g3)/3)

    #Calculate the player's handicap

    handicap = int((200 - average)*0.8)

    #Print the average and handicap

    print("The bowler's average is:",average)
    print("The bowler's handicap is:",handicap)
    
main()
