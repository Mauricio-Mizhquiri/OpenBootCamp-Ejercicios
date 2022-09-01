
from tkinter import ttk
import tkinter as tk

import tkinter
windows = tkinter.Tk()

select = tkinter.StringVar()

label1 = tkinter.Label(windows, text= 'Lista de frutas', foreground="Green")
label1.grid(row=0, column=1, sticky=tkinter.W, ipadx= 5, ipady= 5)  

#Label para mostrar la información de la seleccion
label2 = tkinter.Label(windows, text= '', foreground="Green")
label2.grid(row=7, column=1, sticky=tkinter.W, ipadx= 5, ipady= 5) 

#Creando funciones necesarias
def getTextSelection(event):
    label2.config(text = select.get())

#método para reiniciar la seleccion de los radioButton
def reiniciar(event):
    label2.config(text = '')
    select.set(0)


#método para salir del programa
def salir(event):
    print('Saliendo')
    windows.quit()



#Creando los radioButtons

#Creando el radiobutton manzana
r1 = ttk.Radiobutton(windows, text="Manzana",value="Manzana", variable=select)    
r1.bind("<Button-1>",getTextSelection)
r1.grid(row=2, column=0,padx=10,pady=10)

#Creando el radiobutton pera
r2 = ttk.Radiobutton(windows, text="Pera",value="Pera", variable=select)    
#r2.pack()
r2.bind("<Button-1>",getTextSelection)
r2.grid(row=3, column=0,padx=10,pady=10)

#Creando el radiobutton Sandia
r3 = ttk.Radiobutton(windows, text="Sandia",value="Sandia", variable=select)    
r3.bind("<Button-1>",getTextSelection)
r3.grid(row=4, column=0,padx=10,pady=10)

#Creando el radiobutton platano
r4 = ttk.Radiobutton(windows, text="Platano",value="Platano", variable=select)    
r4.bind("<Button-1>",getTextSelection)
r4.grid(row=5, column=0,padx=10,pady=10)

#Creando el radiobutton uva
r4 = ttk.Radiobutton(windows, text="Uva",value="Uva", variable=select)    
r4.bind("<Button-1>",getTextSelection)
r4.grid(row=6, column=0,padx=10,pady=10)


#Creando un button de reiniciar
buttonReiniciar = tkinter.Button(windows, text="Reiniciar")
buttonReiniciar.grid(row=8, column=1, sticky=tkinter.W, padx=15, pady=15)
buttonReiniciar.bind("<Button-1>",reiniciar)

#Creando un button para salir
buttonSalir = tkinter.Button(windows, text="Salir")
buttonSalir.grid(row=8, column=2, sticky=tkinter.W, padx=15, pady=15)
buttonSalir.bind("<Button-1>",salir)


windows.mainloop()