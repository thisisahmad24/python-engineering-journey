class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Ali", 90)
s2 = Student("Sara", 85)

print("Students:")
print(s1.name, s1.marks)
print(s2.name, s2.marks)

# object independence
s1.name = "Ahmad"
s2.name = "Lina"
s1.marks = 95
s2.marks = 88
print("\nAfter change:")
print("s1:", s1.name)
print("s1 marks:", s1.marks)
print("s2:", s2.name)
print("s2 marks:", s2.marks)