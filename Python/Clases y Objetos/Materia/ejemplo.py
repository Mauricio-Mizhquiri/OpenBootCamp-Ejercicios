class Dino:
    _encendido = True 
    
    #Funciones
    def apaga(self):
        print('Apaga el aparato')

    def isEncendido(self):
        return self._encendido

#Ejemplo de ejecución
d = Dino()
d.apaga()
print(d.isEncendido())

d2 = Dino()
print(d2.isEncendido())

#Clases estáticas
class Estatica:
    numero = 1

    #funciones
    def incrementa():
        Estatica.numero += 1

Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

class Opciones:
    ServidorSeguro = True


#HERENCIA
class Juguete:
    _encendido = True
    def __init__(self):
        print('Estoy en el constructor de la clase Juguete')
    
    #funciones
    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False
    
    def isEncendido(self):
        return self._encendido

class Potato(Juguete):
    def quitarOreja(self):
        pass
    def ponerOreja(self):
        pass




p = Potato()
p.enciende()
print(p.isEncendido())
p.apaga()
print(p.isEncendido())


#Constructores
class Dino(Juguete):
    color = None
    nombre = 'Verde'

    #constructor
    def __init__(self, nombre):
        super().__init__()
        self.color = 'Verde'
        self.nombre = nombre

        print('Estoy en el constructor ')

    #destructot
   # def __del__(self):
       # print('Estoy en el destructor de la clase Dino')  
    #con la palabra reservada 'del' puedo eliminar 
    #cualquier variable 

    def verEscamas(self):
        pass



d = Dino('amigo')
print(d.nombre)

'''No existen las clases en python solamente son diccionarios
'''
_encendido = False
def enciende():
    print('Invoco a enciende')
    global _encendido
    _encendido = True

def apaga():
    global _encendido
    _encendido = False

def isEncendido():
    return _encendido

diccionario = {
    'encendido' : False,
    'enciende' : enciende,
    'apaga' : apaga
}
diccionario['enciende']
print(diccionario['encendido'])