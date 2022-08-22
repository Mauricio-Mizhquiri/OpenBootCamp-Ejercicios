class Alumno:
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print('Nombre: ',self.nombre)
        print('Nota: ',self.nota)


    def resultado(self):
        if self.nota >= 7:
            print('Su nota es', self.nota,',usted aprobó la materia')
        else:
            print('Su nota es',self.nota,',sted no aprobó la materia')

#Definiendo dos alumnos
Juan  = Alumno('Juan',9)
print()
Juan.imprimir()
Juan.resultado()


Maria = Alumno('Maria',6)
print()
Maria.imprimir()
Maria.resultado()