#Ask user about his name and age. 
#Then convert the age to an integer and print a message with the name and age.
name = input('Enter your Name: ')
age = input ('Enter Your Age: ')

age = int(age)
print ('Hello', name + '!')
print ('You are', age, 'years old.')
print ('Next year you will be', age +1, 'years old.')
