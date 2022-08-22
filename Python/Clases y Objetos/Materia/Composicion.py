#Relaciones HAS-A que significa contiene
#y tiene relación ccon composición

class Ventanas:
    cantidad = None
    def __init__(self) -> None:
        self.cantidad = 4

    def cambiarCanrtidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4
class Motor:
    tipo = 'Diesel'

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

#class principal
class Coche:
    motor = Motor()
    Carroceria = Carroceria()

c = Coche()
print('Motor es: ',c.motor.tipo)
print('Ventanas',c.Carroceria.ventanas.cantidad)
c.Carroceria.ventanas.cambiarCanrtidad(3)
print('Ventanas',c.Carroceria.ventanas.cantidad)

