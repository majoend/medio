
from tkinter import *
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado

def enviar():
    texto = entrada.get()
    print(f"BIENVENIDO A PYTHON: {texto}")

def eliminar():
    entrada.delete(len(entrada.get()) - 1, END)

window = Tk()
window.title('ventana nueva')
window.configure(bg='black')  # Fondo tenebroso

# Mensaje "Esto es un virus"
mensaje1 = Label(window, text='¡Esto es un virus!', font=('Courier', 24), fg='red', bg='black')
mensaje1.pack(pady=10)

# Cargar imagen de calavera

img = Image.open('C:\\Users\\Usuario\\OneDrive\\Desktop\\practicando\\medio\\calavera.png') 
img = img.resize((200, 200))  

photo = ImageTk.PhotoImage(img)
imagen = Label(window, image=photo, bg='black')
imagen.pack(pady=10)

# Segundo mensaje debajo
mensaje2 = Label(window, text='Es una bromita jeje 😜', font=('Arial', 10), fg='white', bg='black')
mensaje2.pack(pady=10)

# Campo de entrada
entrada = Entry(window, font=('Arial', 20), background='skyblue', foreground='red')
entrada.pack(pady=10)

# Botones
boton_enviar = Button(window, text='Enviar', command=enviar)
boton_enviar.pack(side=RIGHT, padx=5)

boton_eliminar = Button(window, text='Eliminar', command=eliminar)
boton_eliminar.pack(side=RIGHT)

window.mainloop()
