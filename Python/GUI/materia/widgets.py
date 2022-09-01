#Creando un frame
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser


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

'''selected = tkinter.StringVar()
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
'''

#Usando el checkBox
#selected = tkinter.StringVar()
#command = miFuncion para hacer que algo se haga al presionar el ejemplo
#def miFuncion():
 #   print("Has clickeado")

#checkbox = ttk.Checkbutton(window, text="acepto las condiciones", variable=selected, command = miFuncion)
#checkbox.grid(row=0, column=0)

#Revisando el tema de eventos
#Evento: cuando se hace algo en un sistema

'''
def saludar(event):
    print('Han hecho click en saludar')

def saludarDobleClick(event):
    print("Saludando con doble click")

def salir(event):
    print('adios')
    window.quit()

button = tkinter.Button(window, text="Haz click")
button.pack()
button.bind("<Button-1>",saludar)
button.bind("<Double-1>",saludarDobleClick)

#Boton de salir
buttonSalir = tkinter.Button(window, text="Salir")
buttonSalir.pack()
buttonSalir.bind("<Button-1>",salir)'''

#haciendo dialogos
#filename = filedialog.askopenfilename()
colorchooser.askcolor(initialcolor = '#fff')

window.mainloop()