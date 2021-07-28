#  File: Report.py
#  Description: A formatted company report with modifiable variables
#  Student's Name: Enrique Martinez
#  Student's UT EID: egm657
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 3/5/2020
#  Date Last Modified: 3/6/2020


def main():

     # input data
    companyName = "Lone Star Corporation"
    date = "March 5, 2020"
    cash = 7505.54
    acctsRec = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machAndEquip = 8329.99
    patents = 2000.00
    acctsPay = 93569.23
    stock = 88100.00

    strFrm = "^80s"
    fltFrm1 = ">9.2f"
    fltFrm2 = ">10.2f"
    colOne = "<31s"
    colTwo = "<30s"
    blank = ""
    indent = "   "
    
    print(format(blank,strFrm))
    print(format(companyName.upper(),strFrm))
    print(format("Balance Sheet",strFrm))
    print(format(date,strFrm))
    print(format(blank,strFrm))
    print(format(blank,strFrm))
    print(format(blank,colOne)+indent*3+format((indent+"Liabilities and"),colOne))
    print(format("Assets",colOne)+indent*3+format((indent*2+"Stockholders' Equity"),colOne))
    print("-"*80)
    print(format((indent+ "Cash"),colOne)+format(cash,fltFrm1)+indent+format("Liabilities:",colOne))
    print(format((indent+ "Accounts Receivable"),colOne)+format(acctsRec,fltFrm1)+format((indent*2+"Accounts Payable"),colTwo)+format(acctsPay,fltFrm2))
    print(format((indent+ "Supplies"),colOne)+format(supplies,fltFrm1)+ " "*40)
    print(format((indent+ "Land"),colOne)+format(land,fltFrm1)+ " "*40)
    print(format((indent+ "Buildings"),colOne)+format(buildings,fltFrm1)+format((indent*2+"Stockholders' Equity:"),colTwo)+" "*10)
    print(format((indent+ "Machines and Equipment"),colOne)+format(machAndEquip,fltFrm1)+format((indent*3+"Capital Stock"),colTwo)+format(stock,fltFrm2))
    print(format((indent+ "Patents"),colOne)+format(patents,fltFrm1)+ " "*40)
    print(format(blank,strFrm))
    print(format("Total Assets",colOne)+format((cash+acctsRec+supplies+land+buildings+machAndEquip+patents),fltFrm1)+indent+format("Total Liabilities and",colOne))
    print(" "*40+format((indent*2+"Stockholders' Equity"),colTwo)+format((acctsPay+stock),fltFrm2))
    print(" "*80)
main()
