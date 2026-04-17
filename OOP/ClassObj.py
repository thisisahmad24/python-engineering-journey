class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


c1 = Car("Toyota", 5000000)
c2 = Car("Honda", 4000000)

print(c1.brand)
print (c1.price)
print(c2.brand)
print(c2.price)