from flask import Flask, render_template, request, redirect, flash
from storage import load_expenses, save_expenses

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    expenses = load_expenses()
    total = sum(int(e["amount"]) for e in expenses)
    return render_template("index.html", expenses=expenses, total=total)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        desc = request.form["desc"]

        expenses = load_expenses()
        expenses.append({
            "amount": amount,
            "category": category,
            "desc": desc
        })

        save_expenses(expenses)
        flash("Expense added!")
        return redirect("/")

    return render_template("add.html")


@app.route("/delete/<int:index>")
def delete(index):
    expenses = load_expenses()
    expenses.pop(index)
    save_expenses(expenses)
    return redirect("/")


app.run(debug=True)