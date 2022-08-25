f = open('mifichero.txt','w')
#write: solo se escribe el texto que se envia
#writelines: escribe texto que se le pasa con una lista
lista = ['animal\n','amigo\n','araña\n','azo\n']
f.writelines(lista)
f.close()

