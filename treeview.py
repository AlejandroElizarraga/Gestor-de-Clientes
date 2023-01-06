from tkinter import *
from tkinter import ttk

app= Tk()
app.title('Treeview')
app.configure(background='#333333')

tree = ttk.Treeview(app)
tree['columns']=('Nombre','Telefono','Empresa')
#Generas la cantidad de columnas en una tupla#


################## SECCION 1 ##################
# tree.column('#0')
tree.column('#0',width=0,stretch=NO)
#Segunda opcion sirve para ocultar la primera columna 
#Se agregan parametros para ocultarla
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')
#Generas las opciones anteriormente mencionadas#

################## SECCION 2 ##################
# tree.heading('#0', text='id')
tree.heading('#0')
#Segunda opcion sirve para ocultar la primera columna 
#Se quita el texto
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')
tree.grid(row=0,column=0)
#Generas los titulos para las opciones anteriormente mencionadas#

################## SECCION 3 ##################
tree.insert('',END,'Alex',values=('Uno','Dos','Tres'),text='Hello')
tree.insert('',END,'Edith',values=('3','2','1'),text='World')
tree.insert('',END,'Manu',values=('A','L','E'),text='Python')
#Insertas los valores para la tabla generada#
# Argumento #1 # Nivel dentro de la lista
# Argumento #2 # Posicioón donde se agrega
# Argumento #3 # Id donde se inserta
# Argumento #4 # Valores que se insertan pero dentro de una tupla "()"
# Argumento #5 # Texto que se encontrara en la columna id

app.mainloop()