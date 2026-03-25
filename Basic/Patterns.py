#Logic Building via Patterns and Shapes

# Square Pattern
print('Square Pattern:')
for i in range(3):
    for j in range(3):
        print ('*' , end=" ")
    print()
    end= " "

# Rectangle Pattern
print('Rectangle Pattern:')
for i in range (3):
    for j in range(5):
        print('*' , end=" ")
    print()
    end= " "
    
# Right Triangle Pattern
print('Right Triangle Pattern:')
for i in range(6):
    for j in range(i+1):
        print('*', end=" ")
    print()
    end=" "
    
# Left Triangle Pattern
print('Left Triangle Pattern:')
for i in range(6):
    for j in range(6):
        if j < 6 - i -1:
            print(' ', end=" ")
        else:
            print('*', end=" ")
    print()
    end=" "

# Triangle Pattern
print('Triangle Pattern:')
for i in range(6):
    for j in range(6 - i - 1):
        print(' ', end=" ")
    for k in range(2 * i + 1):
        print('*', end=" ")
    print()
    end=" "
    
# Diamond Pattern
print('Diamond Pattern:')
for i in range(6):
    for j in range(6-i-1):
        print(' ', end=" ")
    for k in range(2*i+1):
        print('*', end=" ")
    print()
for i in range(4, -1, -1):
    for j in range(6-i-1):
        print(' ', end=" ")
    for k in range(2*i+1):
        print('*', end=" ")
    print()
    