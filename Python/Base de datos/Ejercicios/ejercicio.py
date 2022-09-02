import sqlite3

def main():
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