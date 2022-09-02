from getpass import getpass
import sqlite3
from types import NoneType

def main():
    username = input('Nombre de usuario: ')
    password = getpass("Contraseña: ")
    insertarUsuario(7,username, password)

def main2():
    username = input('Nombre de usuario: ')
    password = getpass("Contraseña: ")
    if verificaCredenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")


def verificaCredenciales(username, password):
    conn = sqlite3.connect('C:/Users/rolan/Escritorio/OpenBootCamp/Python/Base de datos/Materia/aplicacion.db')
    cursor = conn.cursor()
    query = f'SELECT id FROM users WHERE username = "{username}" AND password = "{password}"'
    print('query a ejecutar: ',query)
    rows  = cursor.execute(query)
    data = rows.fetchone()
    cursor.close()
    conn.close()
    if isinstance(data, NoneType):
        return False

    return True

def insertarUsuario(id, username, password):
    conn = sqlite3.connect('C:/Users/rolan/Escritorio/OpenBootCamp/Python/Base de datos/Materia/aplicacion.db')
    cursor = conn.cursor()
    query = 'INSERT INTO users (id, username, password) VALUES(?,?,?)'


    rows = cursor.execute(query, (id,username,password))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

