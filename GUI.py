

#widget son los elementos de la interfaz gráfica
#ventana es el contenedor principal de la interfaz gráfica

#QUIERE DECIR QUE LOS WIDGETS SON LOS ELEMENTOS QUE CONTIENE LA VENTANA POR DECIRLO ASI

from tkinter import *

crear_ventana = Tk()

crear_ventana.geometry('400x400')  #esto define el tamaño de la ventana

crear_ventana.title('Gorlito') #esto define el título de la ventana

crear_ventana.config(background="#4f9e8a") #esto define el color de fondo de la ventana

crear_ventana.mainloop() #EJECUTA LA VENTANA

# crear_ventana.geometry('600x600')  #ESTA PARTE DEBE ESTAR ANTES DE MAIN LOOP


#esto crea una ventana vacía y la muestra en pantalla
