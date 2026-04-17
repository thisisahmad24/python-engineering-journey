class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.name} has Rs {self.balance}")


# usage
acc = BankAccount("Ahmad", 1000)

acc.deposit(500)
acc.withdraw(200)

acc.show_balance()