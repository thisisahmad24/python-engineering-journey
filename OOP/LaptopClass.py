class Laptop:
    def __init__(self, battery, ram, storage):
        self.battery = battery
        self.ram = ram
        self.storage = storage
        
L1 = Laptop("5000mAh", "8GB", "512GB")
print(L1.battery)
print(L1.ram)
print(L1.storage)
L2 = Laptop("6000mAh", "16GB", "1TB")
print(L2.battery)
print(L2.ram)
print(L2.storage)
