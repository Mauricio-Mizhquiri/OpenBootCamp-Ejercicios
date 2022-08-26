#buscar información de python en docs.python.org

#Programación multihilo
import _thread
from errno import WSAESHUTDOWN
import time

def horarioActual(nombre_thread, tiempo_de_espera):
    count = 0
    while count <= 5:
        time.sleep(tiempo_de_espera)
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')
        count += 1
    	

_thread.start_new_thread(horarioActual,('thread uno',1))
_thread.start_new_thread(horarioActual,('thread dos',2))

print("He disparado ya los hilos")
while True:
    pass