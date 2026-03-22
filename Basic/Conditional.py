name = input("Please enter your name: ")
age = int(input("Please enter your age: ") )

#Conditional Statements to verify Name and Age
if age >= 18:
    print("Welcome, " + name + "! You are eligible to access the content.")
elif age < 18:
    print("Sorry, " + name + ". You are not old enough to access the content.")
else:
    print("Hello, " + name + "! Please provide valid credentials to access the content.")
    