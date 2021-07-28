#  File: Population.py
#  Description: A program that verifies Benford's law for 2009 U.S. Census data
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 5/4/2020
#  Date Last Modified: 5/5/2020



def main():


    
    census = '2009CensusData.txt' # file name that needs to be read
    digit_pop_dict = {}
    with open(census, 'r') as read_file:
        lines = read_file.readlines()[1:]
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            else:
                line = line.split()
                digit = int(line[-1][0])
                if digit_pop_dict.get(digit) == None:
                    digit_pop_dict[digit] = int(line[-1])
                else:
                    digit_pop_dict[digit] = int(line[-1]) + digit_pop_dict.get(digit)



    total_population = sum(digit_pop_dict.values())
    print('{:<5}{:>12}{:>8}'.format('Digit', 'Count', '%'))
    print('-' * 25)
    for i in range(1, 10):
        if digit_pop_dict.get(i) == None:
            population = 0
        else:
            population = digit_pop_dict.get(i)
        print('{:<5}{:>12}{:>8.1f}'.format(i, population, 100 * population / total_population))
    print('-' * 25)


main()
