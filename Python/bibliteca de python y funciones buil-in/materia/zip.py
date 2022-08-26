cursos = ['java','python','git']
aistentes = [15,20,4]
demo = zip(cursos, aistentes)   
print(list(demo))	

#funcines all y any sirve para verificar que todas las condiciones de la lista se cumpplan
lista = [1 == 1, 2 == 2, 3 == 4]
res = all(lista)
print(res)

#funcion round: sirve para redondear al valor mas proximo
a = 5.5
b = 5.4
c = 5.6

print(round(a))
print(round(b))
print(round(c))

#funcion min: sirve para sacar el minimo de una lista de valores
print(min(1,2,3,4,5,6,7,8,10,11,12,13,14,15,))
#funcion max: sirve para sacar el max de una lista de valores
print(min(1,2,3,4,5,6,7,8,10,11,12,13,14,15,))
lista = ['z','e','a','h']
print(sorted(lista))
