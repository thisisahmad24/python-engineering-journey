# polymorphism in python is the ability of an object to take on many forms. It allows us to define methods in the child class with the same name as defined in their parent class. This is one of the core concepts of OOP and it allows for flexibility and reusability of code.
class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for a in animals:
    a.speak()