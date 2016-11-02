def main():
    v_county_sales_tax_rate = 0.02
    v_state_sales_tax_rate = 0.04

    v_total_sales = inputData()
    v_county_tax = calcCountyTax(v_total_sales, v_county_sales_tax_rate)
    v_state_tax = calcStateTax(v_total_sales, v_state_sales_tax_rate)
    v_total_tax = calcTotalTax(v_county_tax, v_state_tax)
    printTax(v_county_tax, v_state_tax, v_total_tax)    


def inputData():
    v_total_sales = input('Enter the total sales for the month.')
    return v_total_sales

def calcCountyTax(v_total_sales, v_county_sales_tax_rate):
    return v_total_sales * v_county_sales_tax_rate

def calcStateTax(v_total_sales, v_state_sales_tax_rate):
    return v_total_sales * v_state_sales_tax_rate

def calcTotalTax(v_county_tax, v_state_tax):
    return v_county_tax + v_state_tax


def printTax(v_county_tax, v_state_tax, v_total_tax):
    print 'The total tax : ', v_total_tax, ' (the state tax : ', v_state_tax, ' and the county tax : ', v_county_tax 


main()
