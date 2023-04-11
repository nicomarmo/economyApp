from tkinter import *


root = Tk()

root.title("EconomyApp")


l1 = Label(
    root,
    text='Ingrese los datos solicitado'
)
###Variables###
ingreso_var = DoubleVar()
monto_var = DoubleVar()
descrip_var = DoubleVar()

###Entrys###
ingreso = Label(root, text='Ingreso')
ingreso.grid(row=2, column=0)
ingreso_e = Entry(root, textvariable=ingreso_var)
ingreso_e.grid(row=2, column=1)

monto = Label(root, text='Gasto')
monto.grid(row=3, column=0)
monto_e = Entry(root, textvariable=monto_var)
monto_e.grid(row=3, column=1)

descrip = Label(root, text='Descripción')
descrip.grid(row=4, column=0)
descrip_e = Entry(root, textvariable=descrip_var)
descrip_e.grid(row=4, column=1)


### Comentario de prueba ###














root.mainloop()