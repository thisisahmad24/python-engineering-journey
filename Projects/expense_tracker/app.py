from flask import Flask, render_template, request, redirect, flash
from storage import load_expenses, save_expenses
from datetime import datetime
from analysis import analyze_expenses

app = Flask(__name__)
app.secret_key = "secret"


#Home Route (Dashboard + Analysis)
@app.route("/")
def index():
    expenses = load_expenses()

    category_percent, total, highest, insights = analyze_expenses(expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        category_percent=category_percent,
        highest=highest,
        insights=insights
    )


#Add Expense
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        desc = request.form["desc"]

        expenses = load_expenses()

        expenses.append({
            "amount": int(amount),
            "category": category.lower(),
            "desc": desc,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

        save_expenses(expenses)
        flash("Expense added successfully!")

        return redirect("/")

    return render_template("add.html")


#Delete Expense
@app.route("/delete/<int:index>")
def delete(index):
    expenses = load_expenses()

    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
        flash("Expense deleted!")

    return redirect("/")


# ▶️ Run App
if __name__ == "__main__":
    app.run(debug=True)