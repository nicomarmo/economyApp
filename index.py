from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()

root.title("EconomyApp")

###Variables###
ingreso_var = DoubleVar()
monto_var = DoubleVar()
descrip_var = StringVar()
el_id = 0

###Entrys###
ingreso = Label(root, text="Ingreso")
ingreso.grid(row=2, column=0)
ingreso_e = Entry(root, textvariable=ingreso_var)
ingreso_e.grid(row=2, column=1)

monto = Label(root, text="Gasto")
monto.grid(row=3, column=0)
monto_e = Entry(root, textvariable=monto_var)
monto_e.grid(row=3, column=1)

descrip = Label(root, text="Descripción")
descrip.grid(row=4, column=0)
descrip_e = Entry(root, textvariable=descrip_var)
descrip_e.grid(row=4, column=1)



###Treeview###
tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3")

tree.column("#0", width=50, minwidth=50, anchor=CENTER)
tree.column("col1", width=100, minwidth=50, anchor=CENTER)
tree.column("col2", width=100, minwidth=50, anchor=CENTER)
tree.column("col3", width=100, minwidth=50, anchor=CENTER)

tree.heading("#0", text="ID")
tree.heading("col1", text="Total actual")
tree.heading("col2", text="Gasto")
tree.heading("col3", text="Descripción")

tree.grid(row=6, column=0, columnspan=4)




###Funciones###

def conec_db():
    con = sqlite3.connect("economydb.db")
    return con

try:
    myConnect = sqlite3.connect("economydb.db")
    cursor = myConnect.cursor()
    cursor.execute(
        "CREATE TABLE gastos1 (id INT(7) NOT NULL PRIMARY KEY, ingreso FLOAT(128), monto FLOAT(128), descripcion VARCHAR(128))"
    )
except Exception as ex:
    print(ex)


def ingreso_func():
    global el_id
    myConnect.commit()
    data = (
        str(el_id),
        str(ingreso_var),
        str(monto_var),
        str(descrip_var),
    )
    sql = "INSERT INTO gastos1(id, ingreso, monto, descripcion) VALUES(?,?,?,?)"
    cursor.execute(sql, data)
    myConnect.commit()
    tree.insert("", "end", text=(el_id),
                values=(ingreso_var.get(), monto_var.get(), descrip_var.get()))
    el_id += 1






###Botones###

###Boton Crear###
ingreso_b = Button(
    root, text='Ingreso', command=ingreso_func, relief=RAISED, width=10)
ingreso_b.grid(row=2, column=2, padx=(10, 10), pady=(10, 10))

###Boton xxx###

root.mainloop()