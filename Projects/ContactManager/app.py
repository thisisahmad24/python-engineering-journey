from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

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


@app.route("/")
def index():
    contacts = load_contacts()
    return render_template("index.html", contacts=contacts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]

        contacts = load_contacts()
        contacts.append({"name": name, "phone": phone})
        save_contacts(contacts)

        return redirect("/")

    return render_template("add.html")


@app.route("/delete/<name>")
def delete(name):
    contacts = load_contacts()
    contacts = [c for c in contacts if c["name"] != name]
    save_contacts(contacts)
    return redirect("/")


@app.route("/search", methods=["GET", "POST"])
def search():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        contacts = load_contacts()

        result = [c for c in contacts if name.lower() in c["name"].lower()]

    return render_template("search.html", result=result)


app.run(debug=True)