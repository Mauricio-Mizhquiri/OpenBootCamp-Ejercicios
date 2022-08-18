def numeroPrimo(numero):
    for num in range(2,numero):
        if numero%num == 0:
            return False
    return True


numero = 6
if(numeroPrimo(numero)):
    print("El numero", numero, 'es primo')
else:
    print('El numero',numero,'no es primo')