class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


students = [
    Student("Ali", 40),
    Student("Sara", 80),
    Student("Ahmad", 60)
]

result = {}

for s in students:
    key = "pass" if s.marks > 50 else "fail"
    result[key] = result.get(key, 0) + 1

print(result)