# Kiyoung Park, Oct 26th, 2016
# Lab 5-5 – Programming Challenge 1 – Yum Yum Burger Joint# This program is to calculate total payment for order

# This is main function
def main():
    #initialize variables
    endProgram = 'no';
    #Loop to run program again
    while endProgram == 'no':
        #reset variables
        totalBurger = 0
        totalFry = 0
        totalSoda = 0
        total = 0
        endOrder = 'no'
        #Loop to take in order
        while endOrder == 'no':
            print 'Enter 1 for Yum Yum Burger'
            print 'Enter 2 for Grease Yum Fries'
            print 'Enter 3 for for Soda Yum'
            option = input('Enter now -> ')
            if option == 1:
                totalBurger = getBurger(totalBurger)
            elif option == 2:
                totalFry = getFry(totalFry)
            elif option == 3:
                totalSoda = getSoda(totalSoda)
            endOrder = raw_input('Do you want to end your order?(Enter no to add more items): ')
    
        total = calcTotal(totalBurger, totalFry, totalSoda)
        printReceipt(total)

        endProgram = raw_input('Do you want to end the program?(Enter no to proess a new order): ')

# This is calculate totalBurget
def getBurger(totalBurger):
    burgertCount = input('Enter the number of burgers you want: ')
    totalBurger = totalBurger + ( burgertCount * .99 )
    return totalBurger

# This is calculate totalFry
def getFry(totalFry):
    fryCount = input('Enter the number of fries you want: ')
    totalFry = totalFry + ( fryCount * .79 )
    return totalFry

# This is calculate totalSoda
def getSoda(totalSoda):
    sodaCount = input('Enter the number of sodas you want: ')
    totalSoda = totalSoda + ( sodaCount * 1.09 )
    return totalSoda

# This is calculate total price
def calcTotal(totalBurger, totalFry, totalSoda):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal * .06
    total = subtotal + tax
    return total

# This is print receipt
def printReceipt(total):
    print 'Your total is $' , total
    

main()
