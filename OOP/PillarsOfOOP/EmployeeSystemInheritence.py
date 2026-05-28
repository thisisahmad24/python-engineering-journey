class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


m1 = Manager("Ahmad", 120000, "AI")

m1.show()

print(m1.department)