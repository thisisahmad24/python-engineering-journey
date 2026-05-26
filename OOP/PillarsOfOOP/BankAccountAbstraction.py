class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Ahmad", 1000)

acc.deposit(500)
acc.withdraw(200)

print(acc.get_balance())