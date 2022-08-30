
#Posicionamiento mediante plays
#para posicionar de forma relativa dentro de una ventana
import tkinter
from tkinter import ttk

window = tkinter.Tk()   
label1 = ttk.Label(window, text='Posicionamiento absoluto', background= 'blue', foreground= 'white')
label1.place(x = 10, y = 50)

label2 = ttk.Label(window, text='Otro mas', background= 'red', foreground= 'yellow')
label2.place(x = 25, y = 30)




window.mainloop()


