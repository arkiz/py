# Kiyoung Park, OCT 17th, 2016
# This program will caculate tip, tax and total price of meal

# This is main function
def main():
    mealPrice = getMealPrice()
    tip = calcTip(mealPrice)
    tax = calcTax(mealPrice)
    total = calcTotal(mealPrice, tip, tax)
    printPrice(mealPrice, tip, tax, total)

# gets a meal price
def getMealPrice():
    mealPrice = input("Enter the meal price $ ")
    return mealPrice

# calculates tip by the meal price
def calcTip(mealPrice):
    tipPercent = 0
    if mealPrice >= 25.01:
        tipPercent = 22
    elif mealPrice < 25.01 and mealPrice >= 17.01:
        tipPercent = 19
    elif mealPrice < 17.01 and mealPrice >= 12.01:
        tipPercent = 16
    elif mealPrice < 12.01 and mealPrice >= 6:
        tipPercent = 13
    elif mealPrice < 6 and mealPrice >= 0.01:
        tipPercent = 10
    tip = mealPrice * (float(tipPercent)/100)
    return tip

# calculates tax by the meal price
def calcTax(mealPrice):
    tax = mealPrice * 0.06
    return tax

# calculates total price
def calcTotal(mealPrice, tip, tax):
    total = mealPrice + tip + tax
    return total

# print meal price with tip and tax
def printPrice(mealPrice, tip, tax, total):
    print "The meal price is $ ", mealPrice
    print "The meal tip is $ ", tip
    print "The meal tax is $ ", tax
    print "The total price is $ ", total    

# calls main
main()

            
