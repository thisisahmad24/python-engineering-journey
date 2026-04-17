class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def show(self):
        print(f"{self.category}: {self.amount}")

    def is_expensive(self):
        return self.amount > 1000


e1 = Expense("Food", 500)
e2 = Expense("Travel", 3000)

e1.show()
print(e1.is_expensive())

e2.show()
print(e2.is_expensive())