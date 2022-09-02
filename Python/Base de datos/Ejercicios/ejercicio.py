import sqlite3
from typing import Tuple


def main():
    name = input('Ingrese nombre: ')
    apellido = input("Ingrese apellido: ")
    realizarBusqueda(name, apellido)

def realizarBusqueda(nombre, apellido):
    conn = sqlite3.connect('C:/Users/rolan/Escritorio/OpenBootCamp/Python/Base de datos/Ejercicios/Alumnos.db')
    cursor = conn.cursor()
    query = f'SELECT * FROM Alumnos WHERE nombre = "{nombre}" AND apellido = "{apellido}"'
    rows = cursor.execute(query)
    data = rows.fetchone()
    if isinstance(data, Tuple):
        print('\t\nAlumno encontado sus datos son:\n')
        print('Id: ',data[0])
        print('Nombre: ',data[1])
        print('Apellido: ',data[2])
    else:
        print('Alumno no encontrado')	

def main2():
    for i in range(4):
        id = int(input('Ingrese el id del alumno: '))
        name = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        insertarAlumnos(id, name, apellido)    

def insertarAlumnos(id,name,apellido):
    conn = sqlite3.connect('C:/Users/rolan/Escritorio/OpenBootCamp/Python/Base de datos/Ejercicios/Alumnos.db')
    cursor = conn.cursor()
    query = 'INSERT INTO Alumnos (id, nombre, apellido) VALUES(?,?,?)'
    rows = cursor.execute(query, (id,name,apellido))
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()