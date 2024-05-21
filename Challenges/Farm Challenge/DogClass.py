from AnimalsClass import *

class Cow(Animal):
    def __init__(self, name, race):
        super().__init__(name, race)
        
    def moo(self): print(f"The {self.race} cow, {self.name} is mooing. MOO! MOO!")
