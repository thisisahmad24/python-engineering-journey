class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


def average_marks(students):
    total = 0

    for s in students:
        total += s.marks

    return total / len(students)


students = [
    Student("Ali", 40),
    Student("Sara", 80),
    Student("Ahmad", 60)
]

print("Average:", average_marks(students))