# While Loop
print('Numbers in while loop:')
i = 0
while i < 5:
    print(i)
    i += 1

# While loop with break and continue
print('While loop with break and continue:')
i = 0
while i< 10:
    if i == 10:
        break
    if i % 2 == 0:
        i += 1
        continue
    print (i)
    i += 1

# While loop with else
print('While loop with else:')
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('Loop completed successfully.')
    
# While loop with pattern
print('While loop with pattern:')
i = 0
while i < 7:
    print('*' * (i + 1))
    i += 1
    
# While loop with user input
print('While loop with user input:')
while True:
    user_input = input('Enter a number (or "exit" to quit): ')
    if user_input.lower() == 'exit':
        print('Exiting the loop.')
        break
    try:
        number = int(user_input)
        print('You entered:', number)
    except ValueError:
        print('Invalid input. Please enter a valid number or "exit".')
        
# While loop with nested while loop
print('While loop with nested while loop:')
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(i, j)
        j += 1
    i += 1
    