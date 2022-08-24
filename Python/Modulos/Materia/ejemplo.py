#Un modulo es un fichero en python
import operacion as o
import pprint
import sys
import operaciones.suma


def main():
    op = o.Operador()
    print("Valor de la multiplicación es: ",op.multiplicacion(4,5))
    #pprint.pprint(sys.path)
    print(operaciones.suma.suma(4,5))
    print(dir(operaciones))

if __name__ == '__main__':
    main()
    

