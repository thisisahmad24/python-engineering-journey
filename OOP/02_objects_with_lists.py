class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


students = [
    Student("Ali", 40),
    Student("Sara", 80),
    Student("Ahmad", 60)
]

for s in students:
    print(s.name, s.marks)