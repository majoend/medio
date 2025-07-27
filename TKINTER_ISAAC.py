
from tkinter import *
def enviar():
    texto = entrada.get()
    print(f"BIENVENIDO A PYTHON: {texto}")

def eliminar():
    entrada.delete( len(entrada.get()) - 1, END)

window = Tk()
window.title('ventana nueva')

entrada = Entry(window, font=('Arial', 20),
                background='skyblue',
                foreground='red',)

boton_enviar = Button(window, text='Enviar', command=enviar)
boton_enviar.pack(side=RIGHT)

boton_eliminar = Button(window, text='Eliminar', command=eliminar)
boton_eliminar.pack(side=RIGHT)

entrada.pack()
window.mainloop()