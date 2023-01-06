from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 

import sys
print(sys.executable)

app= Tk()
app.title('Treeview')

cnet = sqlite3.connect('crm.db')
c = cnet.cursor()
c.execute("""
            CREATE TABLE if not exists cliente(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                empresa TEXT NOT NULL
            );
          """)

def render_Clientes():
    rows = c.execute("SELECT * FROM cliente").fetchall()

    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("",END,row[0],values=(row[1],row[2],row[3]))

def insertar(cliente):
    c.execute("""
              INSERT INTO cliente (nombre, telefono, empresa) VALUES (?, ?, ?)
              """,(cliente['nombre'],cliente['telefono'],cliente['empresa'],))
    cnet.commit()
    render_Clientes()

def addC():
    def guardar():
        if not nombre.get():
            messagebox.showerror('Error', 'El nombre es obligatorio')
            return
        if not telefono.get():
            messagebox.showerror('Error', 'El teléfono es obligatorio')
            return
        if not empresa.get():
            messagebox.showerror('Error', 'El campo empresa es obligatorio')
            return
        
        cliente={
            'nombre':nombre.get(),
            'telefono':telefono.get(),
            'empresa':empresa.get(),
        }
        insertar(cliente)
        top.destroy()
    top =Toplevel()
    top.title('Nuevo Cliente')
    top.configure(background='#444444')

    lnombre = Label(top,text='Nombre', background='#444444', fg='#eeeeee')
    nombre = Entry(top,width=40)
    lnombre.grid(row=0,column=0, padx=5, pady=5)
    nombre.grid(row=0,column=1, padx=5, pady=5)

    ltelefono = Label(top,text='Teléfono', background='#444444', fg='#eeeeee')
    telefono = Entry(top,width=40)
    ltelefono.grid(row=1,column=0, padx=5, pady=5)
    telefono.grid(row=1,column=1, padx=5, pady=5)

    lempresa = Label(top,text='Empresa', background='#444444', fg='#eeeeee')
    empresa = Entry(top,width=40)
    lempresa.grid(row=2,column=0, padx=5, pady=5)
    empresa.grid(row=2,column=1, padx=5, pady=5)

    save =Button(top,text='Guardar',command=guardar)
    save.grid(row=3,column=1, pady=5)

    nombre.focus()
    top.bind('<Return>',lambda x: guardar())
    top.mainloop()
def removeC():
    id = tree.selection()[0]

    cliente = c.execute("SELECT * FROM cliente WHERE id = ?",(id, )).fetchone()
    respuesta = messagebox.askokcancel('¿Seguro?','¿Estas Seguro de querer eliminar el cliente: "'+ cliente[1] + '" del registro?' )
    if respuesta:
        c.execute("DELETE FROM cliente WHERE id = ?",(id, ))
        cnet.commit()
        render_Clientes()
    else:
        pass

btnN =Button(app,text='Nuevo Cliente',command=addC)
btnR=Button(app,text='Eliminar Cliente',command=removeC)

btnN.grid(row=0,column=0)
btnR.grid(row=0,column=1)

tree = ttk.Treeview(app)
tree['columns']=('Nombre','Telefono','Empresa')

tree.column('#0',width=0,stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Teléfono')
tree.heading('Empresa', text='Empresa')
tree.grid(row=1,column=0,columnspan=2)


render_Clientes()
app.mainloop()