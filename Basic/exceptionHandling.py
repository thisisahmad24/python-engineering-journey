#Exception handling in Python is done using try-except blocks. 
#This allows you to catch and handle exceptions gracefully without crashing the program.  

try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result = num1 / num2
    print("The result of division is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")