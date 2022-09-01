from select import select
from tkinter import ttk

import tkinter
windows = tkinter.Tk()

label1 = tkinter.Label(windows, text= 'Lista de frutas', foreground="Green")
label1.grid(row=0, column=1, sticky=tkinter.W, ipadx= 5, ipady= 5)   

#Creando funciones necesarias
def funcionManzana(event):
    print("Haz seleccionado manzana")

def funcionPera(event):
    print("Haz seleccionado pera")

def funcionSandia(event):
    print("Haz seleccionado Sandia")

def funcionPlatano(event):
    print("Haz seleccionado platano")

def funcionUva(event):
    print("Haz seleccionado Uva")


select = tkinter.StringVar()



#método para reiniciar la seleccion de los radioButton
def reiniciar(event):
    print('Reiniciado')
    select.set(0)


#método para salir del programa
def salir(event):
    print('Saliendo')
    windows.quit()



#Creando los radioButtons

#Creando el radiobutton manzana
r1 = ttk.Radiobutton(windows, text="Manzana",value="1", variable=select)    
r1.bind("<Button-1>",funcionManzana)
r1.grid(row=2, column=0,padx=10,pady=10)

#Creando el radiobutton pera
r2 = ttk.Radiobutton(windows, text="Pera",value="2", variable=select)    
#r2.pack()
r2.bind("<Button-1>",funcionPera)
r2.grid(row=3, column=0,padx=10,pady=10)

#Creando el radiobutton Sandia
r3 = ttk.Radiobutton(windows, text="Sandia",value="3", variable=select)    
r3.bind("<Button-1>",funcionSandia)
r3.grid(row=4, column=0,padx=10,pady=10)

#Creando el radiobutton platano
r4 = ttk.Radiobutton(windows, text="Platano",value="4", variable=select)    
r4.bind("<Button-1>",funcionPlatano)
r4.grid(row=5, column=0,padx=10,pady=10)

#Creando el radiobutton uva
r4 = ttk.Radiobutton(windows, text="Uva",value="5", variable=select)    
r4.bind("<Button-1>",funcionUva)
r4.grid(row=6, column=0,padx=10,pady=10)


#Creando un button de reiniciar
buttonReiniciar = tkinter.Button(windows, text="Reiniciar")
buttonReiniciar.grid(row=7, column=1, sticky=tkinter.W, padx=15, pady=15)
buttonReiniciar.bind("<Button-1>",reiniciar)

#Creando un button para salir
buttonSalir = tkinter.Button(windows, text="Salir")
buttonSalir.grid(row=7, column=2, sticky=tkinter.W, padx=15, pady=15)
buttonSalir.bind("<Button-1>",salir)

windows.mainloop()