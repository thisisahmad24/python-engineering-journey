import json

FILE = "contacts.json"

def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_contacts(data):
    with open(FILE, "w") as f:
        json.dump(data, f)