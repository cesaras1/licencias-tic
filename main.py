from tkinter import *
from tkinter import ttk


"""  crear un marco de GUI con Tkinter """
root = Tk() 
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)



root.resizable(1,1)
root.title("Aplicacion manejo licencias e inventario software")
ancho_ventana = 700
alto_ventana = 300
#leer la resolucion de la pantalla
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)

lbl_saludo = Label(root, text ="Hello World") 
lbl_saludo.pack()


root.update
print ( root.winfo_reqwidth())


root.mainloop()