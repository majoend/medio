
#--------# Proyecto: Reloj Digital

#importamos las librerias

#compound= permite correr el texto a un lado de la imagen
"""
compound='left': el texto a la derecha de la imagen
compound='right': el texto a la izquierda de la imagen
compound='top': el texto debajo de la imagen
compound='bottom': el texto encima de la imagen
compound='center': el texto sobre la imagen
etiqueta = Label(ventana, text="Hola", image=foto, compound='left')
"""

from tkinter import *
from time import strftime 

mi_ventana = Tk()
mi_ventana.title('Digital Clock') #nombre para la ventana

def tiempo(): #funcion para actualizar la hora
    hora_actual = strftime('%H:%M:%S %p')
    etiqueta.config(text=hora_actual)
    etiqueta.after(1000, tiempo)

etiqueta = Label(mi_ventana, font=('calibri', 40, 'bold'), 
                 background='light blue', 
                 foreground='black') #aspecto del reloj 

etiqueta.pack(anchor='center') #
tiempo()  # Llama a la función para iniciar el reloj
mi_ventana.mainloop()