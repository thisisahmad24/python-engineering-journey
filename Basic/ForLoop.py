# For loop
print('Numbers in for loop:')
for i in range(5):
    print(i)
    
# Double for loop
print('Double for loop:')
for i in range(2):
    for j in range(2):
        print(i, j)
        
# For loop with list
print('For loop with list:')
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    
# For loop with string
print('For loop with string:')
for char in 'Hello':
    print(char)
    
# For loop with pattern
print('For loop with pattern:')
for i in range(7):
    print('*' * (i + 1))
    
# For loop with break and continue
print('For loop with break and continue:')
for i in range(10):
    if i == 10:
        break
    if i % 2 == 0:
        continue
    print(i)
    
# For loop with else
print('For loop with else:')
for i in range(5):
    print(i)
else:
    print('Loop completed successfully.')
    