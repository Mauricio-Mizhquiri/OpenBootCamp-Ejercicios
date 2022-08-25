numero = 5
texto = 'quijote'
otroMas = 1.2

def suma(a,b):
    return a + b

#tipos de formas de impresiones de texto con la sentencia print
print('El numero es %d y el texto es %s y el float es %f'%(numero,texto,otroMas))
print('valor flotante %.1f'%otroMas)
print(f'El numero es {numero} y el texto {texto} y otro{otroMas}')
print("El numero es {} y el texto {} y otro mas {}".format(numero,texto,otroMas))
print("El numero es {2} y el texto {1} y otro mas {0}".format(numero,texto,otroMas))
print("El numero es {numero} y el texto {texto} y otro mas {otromas}".format(numero = numero,texto = texto,otromas = otroMas))
print(f'El numero es {numero} y el texto es {texto} y tiene {otroMas}')
print(f'La suma es {suma(50,14)}')


#Diferencias estre type y repr
num = 511
print(type(num))

numText = str(num)
print(type(numText))

print(repr(num))
print(numText)




