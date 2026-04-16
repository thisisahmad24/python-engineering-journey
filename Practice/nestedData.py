users = [
    {"name": "Ali", "age": 20},
    {"name": "Ahmad", "age": 17},
    {"name": "Sara", "age": 22}
]

# Get Names
names = [u["name"] for u in users]
print (names)

# Get Ages
ages =[u["age"] for u in users]
print(ages)