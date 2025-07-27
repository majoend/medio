

from tkinter import *

def convertir():
    unidad = opcion.get()
    valor = float(campo_entrada.get())
    
    if unidad == "Metros a kilómetros":
        resultado = valor / 1000
    elif unidad == "Metros a centímetros":
        resultado = valor * 100
    elif unidad == "Metros a milímetros":
        resultado = valor * 1000
    elif unidad == "Kilómetros a millas":
        resultado = valor / 1.609
    elif unidad == "Centímetros a milímetros":
        resultado = valor * 10
    else:
        resultado = "Opción no válida"
    
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

# Crear ventana
mi_ventana = Tk()
mi_ventana.title("Conversor de medidas")
mi_ventana.geometry("400x300")
mi_ventana.config(bg="#eef")

# Campo de entrada
campo_entrada = Entry(mi_ventana, font=("Arial", 14))
campo_entrada.pack(pady=10)

# Menú desplegable
opciones_conversion = [
    "Metros a kilómetros",
    "Metros a centímetros",
    "Metros a milímetros",
    "Kilómetros a millas",
    "Centímetros a milímetros"
]
opcion = StringVar()
opcion.set(opciones_conversion[0])  # valor por defecto

menu = OptionMenu(mi_ventana, opcion, *opciones_conversion)
menu.pack(pady=10)

# Botón de conversión
boton_convertir = Button(mi_ventana, text="Convertir", command=convertir)
boton_convertir.pack(pady=10)

# Etiqueta de resultado
etiqueta_resultado = Label(mi_ventana, 
                           text="Resultado: ", 
                           font=("Arial", 16), 
                           bg="#eef")

etiqueta_resultado.pack(pady=20)

# Ejecutar la aplicación
mi_ventana.mainloop()
