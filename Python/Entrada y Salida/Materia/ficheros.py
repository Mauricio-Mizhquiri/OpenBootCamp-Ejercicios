#Para leer un fichero se necesita un permiso que hay 3 que son los siguientes
#'r': lectura
#'a': adjuntar informacion
#'w': escritura
#'x': create


f = open('C:/Users/rolan/Escritorio/OpenBootCamp/Python/Entrada y Salida/Materia/fichero.txt', 'rt')
datos  = f.read(10) #sirve para leer los datos que contiene el fichero
datos = f.readline() #lee solo una linea
print(datos)
#para imprimir todo el conjunto de datos
datos = None
while datos != '':
    datos = f.readline()
    print(datos)
f.close()
#para leer el fichero con un for
f = open('C:/Users/rolan/Escritorio/OpenBootCamp/Python/Entrada y Salida/Materia/fichero.txt', 'rt')

print('Leyendo dentro de un for')
datos = f.readlines()
for valor in datos:
    print(valor)

f.close()#Se usa para cerrar el fichero y ademas es una buena practica de programación

