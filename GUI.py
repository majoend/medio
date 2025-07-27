#widget son los elementos de la interfaz gráfica
#ventana es el contenedor principal de la interfaz gráfica

#QUIERE DECIR QUE LOS WIDGETS SON LOS ELEMENTOS QUE CONTIENE LA VENTANA POR DECIRLO ASI
from tkinter import *
crear_ventana = Tk()

crear_ventana.geometry('400x400')  #esto define el tamaño de la ventana
crear_ventana.title('Gorlito') #esto define el título de la ventana
crear_ventana.config(background="#020303") #esto define el color de fondo de la ventana

#para mostrar etiquetas en la ventana

#LAS ETIQUETAS NO SON INTERACTIVAS, SOLO MUESTRAN INFORMACION
etiqueta = Label(crear_ventana, 
                 text="Gorlo", #se muestra el texto en la ventana
                 bg="#E9B21C",  #color de fondo de la etiqueta
                 fg="black", # color del texto de la etiqueta
                 relief="sunken", #tipo de relieve de la etiqueta
                 bd=10, #ancho del borde de la etiqueta
                padx=20, #espacio horizontal dentro de la etiqueta
                 font=("Times New Roman", 20)) 

etiqueta.pack(padx=50, pady=50) #esto ejecuta la etiqueta en la ventana

#LOS BOTONES SON INTERACTIVOS 

def click_me(): #HE CREADO UNA FUNCION PARA EJECUTAR EL CLICK
    print('Hola me llamo Gorlo, soy un perro loco jaja')
boton = Button(crear_ventana, text= 'Click me', 
               command=click_me, 
               background="green",
               activebackground="green",)
boton.pack()     
crear_ventana.mainloop() #EJECUTA LA VENTANA 


