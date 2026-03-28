# Tuple Return 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def calculate(a,b):
    sum = a+b
    product = a*b
    return sum, product
result = calculate(a,b)
print("Sum:", result[0])
print("Product:", result[1])

