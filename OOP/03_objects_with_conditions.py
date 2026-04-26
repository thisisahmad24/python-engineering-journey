class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


students = [
    Student("Ali", 40),
    Student("Sara", 80),
    Student("Ahmad", 60)
]

print("Passed students:")

for s in students:
    if s.marks > 50:
        print(s.name)