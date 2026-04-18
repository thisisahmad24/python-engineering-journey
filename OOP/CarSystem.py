class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

cars = [
    Car("Toyota", 5000000),
    Car("Honda", 4000000),
    Car("Ford", 3000000)
]

# Print Car Brands and Prices
print("Car Brands and Prices:")
for car in cars:
    print(car.brand, car.price)

# Filter Cars with Price Greater than 4000000
expensive_cars = [car for car in cars if car.price > 4000000]
print("\nExpensive Cars:")
for car in expensive_cars:
    print(car.brand, car.price)
        