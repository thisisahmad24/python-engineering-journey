# Lists in Python are ordered, mutable, and allow duplicate elements.
# They are defined using square brackets [].

list = [1,2,3,4,5]
print (list)
print(list[0]) # Accessing first element
print(list[1:4]) # Slicing the list
list.append(6) # Adding an element to the end of the list
print(list)
list.insert(2, 10) # Inserting an element at a specific index
print(list)
list.remove(3) # Removing an element by value
print(list)
print(list[-2]) # Accessing the second-to-last element

# List with multiple data types
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)

# List of lists (2D list)
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]
        ]
print(matrix)

# List comprehension to create a new list
squared = [x**2 for x in range(1, 6)]
print(squared)

# List methods
numbers = [1, 2, 3, 4, 5]
print(numbers.count(2)) # Count occurrences of an element
print(numbers.index(3)) # Get index of an element
numbers.sort() # Sort the list
print(numbers)
numbers.reverse() # Reverse the list
print(numbers)

# Nested list comprehension to flatten a 2D list
flattened = [num for sublist in matrix for num in sublist]
print(flattened)

# List slicing with step
print(list[::2]) # Get every second element
