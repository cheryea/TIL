from abc import ABC, abstractmethod

class Weapon(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod    
    def skill(self):
        pass

class Sword(Weapon):
    def skill(self):
        print(f'울부짖어라 {self.name}')

class Wand(Weapon):
    def skill(self):
        print(f'흩날려라 {self.name}')