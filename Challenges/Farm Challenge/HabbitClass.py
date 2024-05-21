from AnimalsClass import *

class Habbit(Animal):
    def __init__(self, name, race):
        super().__init__(name, race)

    def sizzle(self): print(f"The {self.race} habbit, {self.name} is sizzling. chhn! chhhn!")
