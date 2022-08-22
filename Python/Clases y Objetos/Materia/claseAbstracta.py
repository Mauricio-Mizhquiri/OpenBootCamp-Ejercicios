'''
    CLASE ABSTRACTA
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sonido():
        pass

    def diHola(self):
        print('Hola')

class Perro(Animal):
    def sonido(self):
        print('Guau')

class Gato(Animal):
    def sonido(self):
        print('Miau')


p = Perro()
p.sonido()
p.diHola()

g = Gato()
g.sonido()
p.diHola()




