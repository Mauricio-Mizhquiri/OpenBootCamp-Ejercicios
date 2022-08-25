class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self,nombre,precio) -> None:
        self.nombre = nombre
        self.precio = precio

    #str se utiliza para imprimir salidas informales
    def __str__(self) -> str:
        return f'Mi nombre es {self.nombre} y mi preio es {self.precio}'

    #repr se utiliza para imprimir salidas técnicas
    def __repr__(self) -> str:
        return f'potato ({self.nombre}, {self.precio})'


#viendo diferencias entre str y repr
j1 = Juguete('potato',10.5)
j2 = Juguete('Dino',3.4)
print(str(j1))
print(repr(j1))
print('\n\n\n')
#Métodos de cádenas de texto
cadena = 'En algun lugar de la mancha'
#metodo capitalize(): pone en mayusculas la primera letra del texto
print(cadena.capitalize())
#Metodo title(): pone en mayuscula la primera letra de cada palabra de un texto
print(cadena.title())
#Método count(): retorna la cantidad de veces que se repite una palabra en un texto
print(cadena.count('a'))
#Método lower() convierte todo el texto a minusculas
print(cadena.lower())
#Método upper(): convierte todo el texto a mayusculas
print(cadena.upper())
        #Tip: se pued usar los metodos concatenados que también se llama shedding
#Método isdigit(): verifica si un texto es numero o no 
print('456'.isdigit())
#método isalnum(): verifica si una cadena es alfanumerico
print('774bb'.isalnum())
#método isalphe: para verificar si un número es alfabeto
print('dg'.isalpha())
#Método strip(): elimina los espacios en blanco de una cadena al principio y al final
        #Existe tambien lstrip(): que elimina espacios de la izquierda pero no de la derecha
        #Existe tambien rstrip(): que elimina los espacios de la derecha pero no de la izquierda
cadena = '          En algun lugar de la mancha'
print(cadena)
print(cadena.strip())
#Método slit(): conviert una cadena a una lista
print(cadena.split())
