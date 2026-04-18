class Product:
    def __init__(self, name , price):
        self.name = name
        self.price = price
        
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
print(p1.name)
print(p1.price)
print(p2.name)
print(p2.price)

#filter products with price greater than 30000
products = [p1, p2]
expensive_products = [p for p in products if p.price > 30000]
for p in expensive_products:
    print(p.name, p.price)
    