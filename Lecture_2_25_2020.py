def main():

    for i in range(1,21):
        print(i)

    print("Done")

main()



def main2():

    for i in range(1,21):
        if i %5 ==0:
            continue
        else:
            
            print(i)

    print("Done")

main2()


def main3():

    for i in range(1,21):
        if i %5 ==0:
            break
        else:
            
            print(i)

    print("Done")

main3()



def main4():

    number = int(input("Enter an integer: "))

    factorsFound = False

    for i in range(2,number):

        if number % i == 0:
            print(number, "is a multiple of",i,"so it can't be prime")
            factorsFound = True
            break
        else:
            print(number, "is not a multiple of",i, "so we're still looking.")
    if factorsFound ==True:
        print(number,"is not prime.")

    else:
        print(number, "is prime.")

main4()


def main5():

    n = int(input("Enter a positive integer: "))

    total = 0
    count = 0

    for i in range(1,n+1):

        if i % 2 == 0:
            continue
        else:
            total += i
            count += 1

    print ("Average is:" total/count)

    
main5()



