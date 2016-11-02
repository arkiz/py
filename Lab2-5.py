#This program demonstrates how to use variables and functions

#the main function
def main():
    print 'Welcome to the tip calculator program'
    print #print a blank line
    name = inputName()
    age = inputAge()
    print 'Hello,', name, '(', age, ')'

    
#this function inputs name
def inputName():
    name = raw_input('Enter your name: ')
    return name

#this function inputs age
def inputAge():
    age = input('Enter your age: ')
    return age

#call main
main()


