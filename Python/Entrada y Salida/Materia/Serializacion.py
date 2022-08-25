import pickle

class Juguete:
    nombre = ''
    precio = 0

    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio


    def getNombre(self):
        return self.nombre

#Para cargar los datos a serializacion
'''j1 = Juguete('potato',10.5)
#serializando en un fichero
f = open('datos.bin','wb')
pickle.dump(j1,f)
f.close()'''
#Para cargar los datos que he serialziado en datos.bin
f = open('datos.bin','rb')
potato = pickle.load(f)
f.close()
print(type(potato))
print(potato.getNombre(), 'precio: ', potato.precio)