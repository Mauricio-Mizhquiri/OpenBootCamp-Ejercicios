from cgitb import text
import tkinter
from tkinter import ttk
windows = tkinter.Tk()

#Configurando las columnas
windows.columnconfigure(0, weight=1)
windows.columnconfigure(1, weight=3)

#Usuario
#etiqueta usuario
usernamen_label = ttk.Label(windows, text= 'Username')
usernamen_label.grid(column=0, row = 0,sticky=tkinter.W, padx=5, pady=5)

#campo usuario
username_entry = ttk.Entry(windows)
username_entry.grid(column=1, row = 0,sticky=tkinter.E, padx=5,pady=5)

#Para el password
#etiqueta password
password_label = ttk.Label(windows, text= "Pasword: ")
password_label.grid( column=0,row=1, sticky=tkinter.W, padx=5, pady=5)

#campo password
password_entry = ttk.Entry(windows, show = '*')
password_entry.grid(column=1, row = 1,sticky=tkinter.E, padx=5,pady=5)

#Para crear un boton
login_button = ttk.Button(windows, text = 'Loggin')
login_button.grid(column=1,row=3,sticky=tkinter.E, padx=5, pady= 5)



windows.mainloop()


