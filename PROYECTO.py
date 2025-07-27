

import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.title('DATOS')

tree = ttk.Treeview(ventana, columns=('Nombre', 
                                      'Edad', 
                                      'Ciudad'),
                                    show='headings')
tree.pack()

tree.heading('Nombre', text='Nombre')
tree.heading('Edad', text='Edad')
tree.heading('Ciudad', text='Ciudad')

tree.column('Nombre', anchor='center')
tree.column('Edad', anchor='center')
tree.column('Ciudad', anchor='center')

data = [
    ('Isaac', 11, 'Barquisimeto'),]

for entry in data:
    tree.insert('', 'end', values=entry)

ventana.mainloop()