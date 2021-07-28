#  File: GuessingGame.py
#  Description: A game which asks the user to guess a secret number
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 2/28/2020
#  Date Last Modified: 2/28/2020

def main():

    secretNum = 1458

    print("Welcome to the guessing game. You have ten tries to guess my number.")

    tries = 0

    guess = int(input("Please enter your guess: "))

    if guess == secretNum:

        print("That's correct! \nCongratulations! You guessed it on the first try!")

    else:

        while guess != secretNum or tries <= 8:

                if (guess < 1 and tries <= 8) or (guess > 9999 and tries <= 8):

                    print("Your guess must be between 0001 and 9999.")
                    guess = int(input("Please enter a valid guess: "))

                elif guess < secretNum and tries <= 8:

                    tries = tries + 1
                    print("Your guess is too low.")
                    print("Guesses so far:", tries)
                    guess = int(input("Please enter your guess: "))

                elif guess > secretNum and tries <= 8:

                    tries = tries + 1
                    print("Your guess is too high.")
                    print("Guesses so far:", tries)
                    guess = int(input("Please enter your guess: "))

                elif guess == secretNum and tries <= 8:

                    tries = tries + 1
                    print("That's correct! \nCongratulations! You guessed it in", tries,"guesses.")
                    break
                
                else:

                    tries = tries + 1
                    print("Game over. You ran out of guesses.")
                    break

main()

        
