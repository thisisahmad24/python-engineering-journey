import json

FILE = "data.json"


# Load Data
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


# Save Data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# Add Entry
def add_entry(amount, category, desc):
    data = load_data()

    new_id = len(data) + 1

    data.append({
        "id": new_id,
        "amount": amount,
        "category": category,
        "desc": desc
    })

    save_data(data)


# Update Entry
def update_entry(entry_id, new_data):
    data = load_data()

    for item in data:
        if item["id"] == entry_id:
            item.update(new_data)

    save_data(data)


# Delete Entry
def delete_entry(entry_id):
    data = load_data()

    data = [item for item in data if item["id"] != entry_id]

    save_data(data)


# Filter by Category
def filter_category(category):
    data = load_data()
    return [d for d in data if d["category"] == category]


# Sort by Amount
def sort_by_amount():
    data = load_data()
    data.sort(key=lambda x: x["amount"])
    return data


# Analyze Data
def analyze():
    data = load_data()

    total = sum(d["amount"] for d in data)

    categories = {}

    for d in data:
        cat = d["category"]
        categories[cat] = categories.get(cat, 0) + d["amount"]

    return total, categories


# Pretty Print
def pretty():
    data = load_data()
    print(json.dumps(data, indent=4))