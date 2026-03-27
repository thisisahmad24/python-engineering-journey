# Take 5 numbers from user → store in list → print sum
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
total_sum = sum(numbers)
print("The sum of the numbers is:", total_sum)

