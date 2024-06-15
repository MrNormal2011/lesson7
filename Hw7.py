class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def dog(self):
        print(f"{self.name} says WOAW!")

class Cat(Animal):
    def cat(self):
        print(f"{self.name} says MEOW!")

Simba = Dog('Simba')
Silver = Cat('Silver')
Silver.cat()
Simba.dog()