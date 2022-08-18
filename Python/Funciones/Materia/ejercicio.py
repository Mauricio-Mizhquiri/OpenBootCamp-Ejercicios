#DEFINICIÓN DE FUNCIONES

def miFuncion(nombre):
    temperatura = 7.0
    print('Hola',nombre,'la temperatura es ',temperatura)


miFuncion('Yamileth')

#Parámetros variables
def suma(*args):
    resultado = 0
    for arg in args:
        resultado+=arg
    print(resultado)

suma(9,5,6,5,6,5)


#Parametros variables con diccionarios
def valores(**kwars):
    for key, valor in kwars.items():
        print(key,valor)

valores(nombre1 ='Juan', nombre2 = 'Daniel')


