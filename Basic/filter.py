num = [1,2,3,4,5,6,7,8,9,10]
# using filter function to filter out even numbers from the list
filtered = list(filter(lambda x: x % 2 == 0, num))
print(filtered)