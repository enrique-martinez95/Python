def triangle(n):

    total = 0

    for i in range(0,n+1):

        total += i

    return total

def main():

    print("   triangular")
    print("    number")
    print ("--------")

    for i in range (1,21):

        print (format(i, "3d"), format(triangle(i),"6d"))

main()

    
