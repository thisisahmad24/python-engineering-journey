# Functions in Python
def greet():
    print("Hello! Welcome to the Python Engineering Journey.")
greet()

# Function with Parameters
def greet_user(name):
    print("Hello, " + name + "! Welcome to the Python Engineering Journey.")
greet_user("Ahmad")
greet_user("Hassan")

# Function with Return Value
def add(a,b):
    return a + b
result = add(5, 3)
print(result)

# Function with Default Parameters
def greet_user(name="Guest"):
    print("Hello, " + name + "! Welcome to the Python Engineering Journey.")
greet_user()
greet_user("Ahmad")

# Function with Variable Number of Arguments
def greet_users(*names):
    for name in names:
        print("Hello, " + name + "! Welcome to the Python Engineering Journey.")
greet_users("Ahmad", "Hassan", "Sara")

# Lambda Function
square = lambda x: x * x
print(square(5))