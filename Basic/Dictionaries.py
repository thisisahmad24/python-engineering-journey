# Dictionaries in Python are unordered collections of key-value pairs.
# They are defined using curly braces {} with key-value pairs separated by a colon :.

# Creating a dictionary
person = {
    "name": "Ahmad",
    "age": 22,
    "course": "SE"
}
print(person)   
print(person["name"]) # Accessing value by key
print(person.get("age")) # Accessing value using get method

# Adding a new key-value pair
person["city"] = "Karachi"
print(person)

# Updating an existing key-value pair
person["age"] = 23
print(person)

# Removing a key-value pair
del person["course"]
print(person)

# Dictionary with multiple data types
mixed_dict = {
    "name": "Ahmad",
    "age": 22,
    "is_student": True,
    "courses": ["SE", "AI", "DS"]
}       
print(mixed_dict)

# Dictionary methods
print(person.keys()) # Get all keys
print(person.values()) # Get all values
print(person.items()) # Get all key-value pairs
print(len(person)) # Get the number of key-value pairs

# Nested dictionary
students = {
    "student1": {
        "name": "Ahmad",
        "age": 22
    },
    "student2": {
        "name": "Hassan",
        "age": 21
    }
}
print(students)

# Dictionary comprehension to create a new dictionary
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)