
#--------# Proyecto: Reloj Digital

#importamos las librerias

from tkinter import *
from time import strftime 

mi_ventana = Tk()
mi_ventana.title('Digital Clock') #nombre para la ventana

def tiempo(): #funcion para actualizar la hora
    hora_actual = strftime('%H:%M:%S %p')
    etiqueta.config(text=hora_actual)
    etiqueta.after(1000, tiempo)

etiqueta = Label(mi_ventana, font=('calibri', 40, 'bold'), 
                 background='black', 
                 foreground='white',) #aspecto del reloj 

etiqueta.pack(anchor='center') #

tiempo()  # Llama a la función para iniciar el reloj

mi_ventana.mainloop()


