import json

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_expenses(data):
    with open(FILE, "w") as f:
        json.dump(data, f)