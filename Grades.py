#  File: Grades.py
#  Description: A file which takes an input of student's grades and writes an output text
#  report file of their class average.
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 4/30/2020
#  Date Last Modified: 5/1/2020


def main():
    row=[]

#  Import the file #  I could only get this to work from my D drive
    
    with open('D:\\gradeInput.txt','r') as read_file:
        for line in read_file:
            line = line.split()
            
# 3 variables: One for total homework scores, one for exams and a list which stores the avg.

            homeworkTotal = 0
            examTotal = 0
            entry = []
            
# Calculates the average for each student in the class, adds to list
            
            for i in range(len(line)):
                if (i==0):
                    name=line[0].split(',')
                    entry.append(name[1])
                    entry.append(name[0])
                    row.append(entry)
                elif i<=15:
                    homeworkTotal+=int(line[i])
                else:
                    examTotal+=int(line[i])
            entry.append(homeworkTotal/15)
            entry.append(examTotal/3)
            entry.append(0.55*homeworkTotal/15+0.45*examTotal/3)

# Saves a report of the student's averages

    with open('D:\\semesterGradeReport.txt','w+') as write_file:
        write_file.write("{0:>37}{1:>7}{2:>7}\n".format("HW","Exam","Final"))
        write_file.write("{0:<15}{1:<15}{2:>7}{3:>7}{4:>7}\n".format("Last Name","First Name","Avg","Avg","Grade"))
        write_file.write("-"*52)
        write_file.write("\n")

        for r in row:
            line = "{0:<15}{1:<15}{2:>7}{3:>7}{4:>7}\n".format(r[0],r[1],round(r[2],1),round(r[3],1),round(r[4],1))
            write_file.write(line)
main()
