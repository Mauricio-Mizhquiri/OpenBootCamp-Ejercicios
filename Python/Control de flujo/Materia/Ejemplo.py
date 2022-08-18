a = 5
b = 6

#Referente al IF
if a >= 5 and b <= 6:
    print("A es mayor o igual a 5 y b es menor o igual a 6")
elif a >= 6:
    print("A es mayor o igual a 6")
else:
    print("No se cumple nada de lo anterior")

print("fin del if") 

#Bucles en Pyhton

#While
contador  = 10
while contador >= 0:
    print("Hola: ",contador)
    contador-=1

#Palabras reservadas break and continue
contador = 0
while contador <= 10:
    contador+=1
    if contador %2 != 0:
        print(contador)
    if contador == 10:
        break

#For
print("bucle for")

lista = [1,2,3,4,5]
for valor in lista:
    print(valor)


#Switch en pyhton
valor = 'juan'
match valor:
    case 'juan':
        print('Hola soy juan')
    case 'daniel':
        print('hola soy daniel')
    case 'patricio':
        print('soy patricio')
    case 'mauricio':
        print('hello soy mauricio')