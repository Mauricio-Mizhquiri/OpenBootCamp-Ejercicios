from re import T
import tkinter
window = tkinter.Tk()
#creando un widgwt
label1 = tkinter.Label(window, text= 'label1',background="yellow", foreground="blue")
label1.pack(ipadx=45,ipady=15, fill = 'x')

#Expand = True: hace que se expanda al centro
#Fill = both hace que se expanda a la izquiera o derecha o de forma exporadea
#size: sirve para posicionar a la izquierda o derecha
label2 = tkinter.Label(window, text= 'label2',background="purple", foreground="white")
label2.pack(ipadx=45,ipady=15, fill = 'x')	

#Generando un label3
label3 = tkinter.Label(window, text= 'label3',background="blue", foreground="white")
label3.pack(ipadx=45,ipady=15, fill='x')

#Generando un label4
label4 = tkinter.Label(window, text= 'label4',background="red", foreground="white")
label4.pack(ipadx=15,ipady=15, side = 'left')

#Generando label 5
label5 = tkinter.Label(window, text= 'label5',background="yellow", foreground="black")
label5.pack(ipadx=15,ipady=15, side = 'left')

#Generando label6
label6 = tkinter.Label(window, text= 'label6',background="green", foreground="white")
label6.pack(ipadx=15,ipady=15, side = 'right')

#Generando un look para que quede abierta la venntan
window.mainloop()
#Se puede posicionar objetos

