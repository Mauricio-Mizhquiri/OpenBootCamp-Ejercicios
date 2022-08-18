from posixpath import split
import pprint
diccionario ={"clave1":12, "clave2":45, "clave3":859, "clave4":57}
pprint.pprint(diccionario)

#Conjuntos en Python
    #Es una lista pero con otros metódos

lista = [1,2,4,1,2,3]
print(lista)

conjunto = {1,2,3,1,2,3}

print(conjunto)

#Operaciones matemáticas en python
a = {0,2,4,6,8}
b = {1,2,3,4,5}

print(a)
print(b)
#Union
print("\nUnion: ",(a|b))

#interseccion
print("\nIntersección: ",a&b)

#diferencia
print("\nDiferencia: ",a-b)

#Diferencia Simetrica
print("\nDiferencia simétrica: ",a^b)

            #Métodos de String
texto = "hola, esto es un textO"
#Capitalize
print(texto.capitalize())

#title
print(texto.title())

#lower
print(texto.lower())

#Upper
print(texto.upper())

#remplazar
print(texto.replace('o','x'))

#buscar
print(texto.find(','))

#poner una cadena en una lista
print(texto.split(' '))

#combinacion de metodods
print(texto.replace(',', ' ').lower().split())

#OPERADORES ARITMETICOS
    #SUMA +
    #RESTA - 
    #MULTIPLICACIoN *
    #DIVISIoN //
    #MODULO %
    #POTENCIACIÓN **
#OPERADORES DE ASIGNACIÓN
    #IGUAL =
    #ASIGNACIÓN +=