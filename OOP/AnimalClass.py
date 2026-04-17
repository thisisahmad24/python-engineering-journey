class Animal:
    def __init__(self, name , sound):
        self.name = name
        self.sound = sound
        
a1 = Animal ("Dog", "Woof")
a2 = Animal ("Cat", "Meow")
print(a1.name, "makes", a1.sound, "sound")
print(a2.name, "makes", a2.sound, "sound")

