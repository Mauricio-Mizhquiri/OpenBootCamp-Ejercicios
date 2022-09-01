import tkinter

windows = tkinter.Tk()
labelNombre = tkinter.Label(windows, text= 'Lista de colores', foreground="Green")
labelNombre.grid(row=0, column=1, sticky=tkinter.W, ipadx= 5, ipady= 5) 

lista = ['Azul', 'Blanco', 'Morado', 'Rojo','Cafe','Negro', 'Verde', 'Rosado']

listBox  = tkinter.Listbox(windows, height = 20, listvariable= tkinter.StringVar(value = lista))
listBox.grid(row=1,column=1,sticky=tkinter.S, ipadx=15, ipady=15) 


windows.mainloop()