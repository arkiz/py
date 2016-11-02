# Kiyoung Park - Oct 5th, 2016
# This program will demonstrate how to use decision statements in Python.
# This program determines if a should be awared

#The main function
def main():
    print 'Welcome to the program'
    monthlySales = getSales() # gets Sales
    #Function call to determine bonus
    isBonus(monthlySales)
    isDayoff(monthlySales)

#This function gets the monthly sales
def getSales():
    monthlySales = input('Enter the monthly sales $')
    monthlySales = float(monthlySales)
    return monthlySales

def isBonus(monthlySales):
    if monthlySales >= 100000:
        print "You have earned a $5,000 bonus!!!"

def isDayoff(monthlySales):
    if monthlySales >= 112500:
        print "All employee get a day off!!!"
        

#calls main
main()
