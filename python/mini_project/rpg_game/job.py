from abc import ABC, abstractmethod
from weapon import Sword, Wand
class Job(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrier(Job):
    allow_weapons = [Sword]

    def __str__(self):
        return '전사'
    
    def attack(self):
        print('전사의 공격')
    

class Mage(Job):
    allow_weapons = [Wand]

    def attack(self):
        print('마법사의 공격')