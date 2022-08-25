import pickle
#class vehiculo
class Vehiculo:
    def __init__(self, tipo, color, motor) -> None:
        self.tipo = tipo
        self.color = color
        self.motor = motor

    def __str__(self) -> str:
        return f'Tipo: {self.tipo}\nColor: {self.color}\nMotor: {self.motor}'

#creando objeto de la clase vehiculo
vehiculo = Vehiculo('Toyota','Azul','350')

print('\n\tObjeto creado')
print(vehiculo)
#Guardando el objeto mediante serializacion
f = open('Python/Entrada y Salida/Ejercicios/objeto.bin','wb')
pickle.dump(vehiculo,f)
f.close()
print('\n\tAcabo de guardar mi objeto')

#recuperando el objeto mediante serializacion
f = open('Python/Entrada y Salida/Ejercicios/objeto.bin','rb')
vehiculo = pickle.load(f)
f.close()
print('\n\tRecupere mi objeto y es el siguiente\n')
print(vehiculo)

