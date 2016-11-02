# Kiyoung Park, Oct 5th, 2016
# This program shows your age, weight, birth month

#The main fuction
def main():
    age = getAge()
    weight = getWeight()
    birthMonth = getMonth()
    correctAnswer(age, weight, birthMonth)

#This function will get age by user
def getAge():
    return input('Enter your age: ')

#This function will get weight by user
def getWeight():
    return input('Enter your weight: ')

#This function will get birth month 
def getMonth():
    return raw_input('Enter your month(string): ')

#This function will compare age, weight and birth month, and show some messages
def correctAnswer(age, weight, birthMonth):
    if age <= 25:
        print 'Congratulations, the age is 25 or less'
    else :
        print "I'm sorry, you too old"

    if weight >= 128:
        print 'Congratulations, the weight is 128 or more'
    else :
        print "You should eat more."

    if birthMonth == 'April':
        print 'Congratulations, the  birth month is April'
    else :
        print "Your birth month is not April"

main()

        
        
