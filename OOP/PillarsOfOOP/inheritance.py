##inheritance is a way to create a new class that is a modified version of an existing class. The new class is called a child class or subclass and the existing class is called a parent class or superclass. The child class inherits all the attributes and methods of the parent class and can also have its own attributes and methods.
class User:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Student(User):   # inherits User
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


s1 = Student("Ahmad", 90)

s1.show()
print(s1.marks)