# Sets in Python are unordered collections of unique elements.
# They are defined using curly braces {}.

set = {1,2,3,4,5}
print(set)

# Set with multiple data types
mix_set = {1, "Hello", False, 3.14}
print(mix_set)

# Set methods
set.add(6) # Adding an element to the set
print(set)
set.remove(3) # Removing an element from the set
print(set)
print(4 in set) # Checking if an element is in the set
print(len(set)) # Getting the number of elements in the set

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # Union of two sets
print(set1.intersection(set2)) # Intersection of two sets
print(set1.difference(set2)) # Difference of two sets
print(set1.symmetric_difference(set2)) # Symmetric difference of two sets

# Set comprehension to create a new set
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)

# Set of sets (nested sets)
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print(nested_set)
