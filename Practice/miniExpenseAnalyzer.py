expenses = [
    {"category": "food", "amount": 500},
    {"category": "travel", "amount": 2000},
    {"category": "food", "amount": 300}
]

total = sum(e["amount"] for e in expenses)

category_total = {}
for e in expenses:
    cat = e["category"]
    category_total[cat] = category_total.get(cat, 0) + e["amount"]

highest = max(category_total, key=category_total.get)

print("Total:", total)
print("Category:", category_total)
print("Highest:", highest)