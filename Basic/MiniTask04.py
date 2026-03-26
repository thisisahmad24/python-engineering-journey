# Build: Simple Calculator
print("Welcome to Basic Calculator!")

# Functions
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: Division by zero is not allowed!"
    else:
        return a/b


print("Enter Your Choice, What Function You Want To Perform!")
print("1. For Addition")
print("2. For Subtraction")
print("3. For Multiplication")
print("4. For Division")
print("5. For Exit")

choice = int(input("Enter Your Choice Here: "))
Number1 = int(input("Enter 1st Number: "))
Number2 = int(input("Enter 2nd Number: "))

# if-else Conditions Depending on choice
if choice ==1:
    print(add(Number1,Number2))
elif choice ==2:
    print(subtract(Number1,Number2))
elif choice ==3:
    print(multiply(Number1,Number2))
elif choice ==4:
    print(divide(Number1,Number2))
elif choice ==5:
    print("Thank You For Using Basic Calculator! Goodbye!")
else:
    print("Invalid User Choice!")
    



