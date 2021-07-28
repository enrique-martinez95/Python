def main():

    total = 0

    for i in range(1,1001):
        total+= i

    print("The total is:", total)

main()

def main2():

    #accumulator pattern

    #initialize a variable where you accumulate the result
    total = 0
    
    #initialize a counter
    number = 1

    #while (I'm not finished)
    while number <1001:
        total += number
        number+= 1

    print("The total is:", total)

main2()


# a program that takes as input a whole positive number and prints out ONLY
# its first digit

def main3():

    answer = "y"

    while answer == "y":

        number = int(input("Enter a number: "))

        while number >= 10:
            number = number //10
            print("The number so far is:",number)

        print(number)

        answer = input("Do you want to try another number? [yn] ")

main3()

def main4():

    number = 8

    fact = initial value

    for i in range(1,number+1):
        fact *= i

    print("The factorial of", number, "is",fact)

main()




    
        
