def analyze_expenses(expenses):
    if not expenses:
        return {}, 0, None, []

    total = sum(e["amount"] for e in expenses)

    category_totals = {}

    for e in expenses:
        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0) + e["amount"]

    # percentage calculation
    category_percent = {
        k: round((v / total) * 100, 2)
        for k, v in category_totals.items()
    }

    # highest spending category
    highest = max(category_totals, key=category_totals.get)

    # insights
    insights = []

    for cat, percent in category_percent.items():
        if percent > 50:
            insights.append(f"⚠️ High spending on {cat} ({percent}%)")

    if total > 10000:
        insights.append("💡 You are spending a lot this month")

    return category_percent, total, highest, insights