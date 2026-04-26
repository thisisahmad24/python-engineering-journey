class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


expenses = [
    Expense("food", 500),
    Expense("travel", 2000),
    Expense("food", 300)
]

# total
total = sum(e.amount for e in expenses)
print("Total:", total)

# category analysis
category_total = {}

for e in expenses:
    category_total[e.category] = category_total.get(e.category, 0) + e.amount

print("Category:", category_total)

# filter
print("High expenses:")
for e in expenses:
    if e.amount > 1000:
        print(e.category, e.amount)