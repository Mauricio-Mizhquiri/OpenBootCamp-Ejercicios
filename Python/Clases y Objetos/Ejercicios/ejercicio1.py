class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None

    def __init__(self, color, ruedas, puertas) -> None:
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas
    
class Coche(Vehiculo):
    Velocidad = None
    Cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada) -> None:
        super().__init__(color, ruedas, puertas)
        self.Velocidad = velocidad
        self.Cilindrada = cilindrada

    def mostrarInformacionCoche(self):
        print('\n\tInformación de mi Coche\n')
        print('Color',self.Color)
        print('Cantidad de ruedas: ',self.Ruedas)
        print('Cantidad de puertas: ',self.Puertas)
        print('Velociad: ',self.Velocidad)
        print('Cilindrada: ',self.Cilindrada)

coche = Coche('Verde',4,5,'180 Km',250)
coche.mostrarInformacionCoche()

