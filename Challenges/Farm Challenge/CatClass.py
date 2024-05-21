from AnimalsClass import *
class Cat(Animal):
    def __init__(self, name, race):
        super().__init__(name, race)

    def meow (self):
        print(f"The {self.race} cat, {self.name} is meowning. meow, meow...")
