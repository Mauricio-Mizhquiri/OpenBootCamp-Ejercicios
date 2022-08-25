f = open('ejerciciofichero.txt','w')
f.write('Mis datos del fichero')
f.close()

datos = input('Ingrese el texto que quiere ingresar en el fichero: ')
f = open('ejerciciofichero.txt', 'w')
f.write(datos)
f.close


