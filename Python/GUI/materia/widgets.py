#Creando un frame
import tkinter
from tkinter import ttk


window = tkinter.Tk()
#window.columnconfigure(0, weight=1)
#window.columnconfigure(1, weight=3)
#frame = ttk.Frame(window, relief='sunken')

#label = ttk.Label(frame, text = 'hola')
#label.grid(row=0, column=0, sticky=tkinter.W, padx=50, pady=50)
#frame.grid(row=0, column=0,sticky=tkinter.W)
#

#Usando lisbox
#lista = ['Windows', 'macOs','Linux','MS DOS','Amiga OS','BeOS','OS/2']
#lista_items = tkinter.StringVar(value=lista)
#listBox  = tkinter.Listbox(window, height = 20, listvariable= lista_items)
#listBox.grid(row=0,column=0,sticky=tkinter.W)

#Usando radioButton

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value='1', variable=selected)
r2 = ttk.Radiobutton(window, text="No", value='2', variable=selected)
r3 = ttk.Radiobutton(window, text="Quiza", value='3', variable=selected)
#Posicionando los radioButtons
r1.grid(row=1, column=0,padx=5, pady=5)
r2.grid(row=2, column=0,padx=5, pady=5)
r3.grid(row=3, column=0,padx=5, pady=5)


selected2 = tkinter.StringVar()
rs1 = ttk.Radiobutton(window, text="Si2", value='12', variable=selected2)
rs1.grid(row=0, column=1,padx=5, pady=5)

window.mainloop()