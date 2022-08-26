#usando las funciones map, filter and reduce
from math import lgamma


numeros = [1,2,3,4,5,6,7,8,9,10]
def miFuncion(x):
    if x % 2 == 0:
        return True
    return False	

resultado = filter(miFuncion,numeros)
#Otra forma de crear funciones usando lambdas
resultado = filter(lambda x: x % 2 == 0,numeros)
print(list(resultado))

#Viendo la función map
def cuadrado(x):
    return x*x
result = map(cuadrado,[2,3,4,5,6,7])
#otra forma de hacerlo es
result = map(lambda x: x*x,[2,3,4,5,6,7])
print(list(result))