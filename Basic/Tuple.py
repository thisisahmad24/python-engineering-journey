# Tuples in Python are ordered, immutable, and allow duplicate elements.
# They are defined using parentheses ().
tuple = (1, 2, 3, 4, 5)
print(tuple)
print(tuple[0]) # Accessing first element
print(tuple[1:4]) # Slicing the tuple

# Tuple with multiple data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

# Tuple of tuples (2D tuple)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matrix)

# Tuple unpacking and packing
person = ("Ahmad", 22, "SE")

name, age, course = person

print(name)
print(age)
print(course)

# Tuple methods
numbers = (1, 2, 3, 4, 5)
print(numbers.count(2)) # Count occurrences of an element
print(numbers.index(3)) # Get index of an element
