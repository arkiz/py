# Kiyoung Park Oct 5th, 2016
# This program is calculation for the meal's tip(20%), tax(6%) and total

#the main function
def main():
    print 'Welcome to the meal calculator program'
    print #prints a blank line

    meal_price = input_meal()
    tip = calc_tip(meal_price)
    tax = calc_tax(meal_price)
    total = calc_total(meal_price, tip, tax)
    print_info(total, meal_price, tip, tax)

#inputs meal price
def input_meal():
    meal_price = input('Enter your meal price: ')
    meal_price = float(meal_price)
    return meal_price

#calculates tip at 20%
def calc_tip(meal_price):
    tip = meal_price * 0.2
    return tip

#calculates tax at 20%
def calc_tax(meal_price):
    tax = meal_price * 0.06
    return tax

#calculates total cost
def calc_total(meal_price, tip, tax):
    total = meal_price + tip + tax
    return total

#print total cost with tip, tax and meal price
def print_info(total, meal_price, tip, tax):
    print 'Your meal price is $', '{:,}'.format(meal_price)
    print 'The tip(20%) is $', '{:,}'.format(tip)
    print 'The tax(6%) is $', '{:,}'.format(tax)
    print 'The total cost is $', '{:,}'.format(total)

#calls main
main()
    

        
