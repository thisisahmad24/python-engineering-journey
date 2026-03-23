# Print numbers 1–10 using Loops:
 # For Loop
for i in range(5):
    print(i)
# While Loop
i = 0
while i< 5:
    print(i)
    i += 1
    
# Ask user password until correct (while)
password = 'python123'
while True:
    userInput = input ('Enter the password: ')
    if userInput == password:
        print('Correct password! Access granted.')
        break
    else:
        print('Incorrect Password Try Again!')
        
# Print square pattern using nested loop:
for i in range(5):
    for j in range(5):
        print('*', end=" ")
    print()