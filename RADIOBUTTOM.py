
from tkinter import *

my_list = ['nanami', 'gojo', 'itadori', 'nobara', 'mono titi']

ventana = Tk()
ventana.geometry('600x600') 
ventana.title('FOOD')



x = IntVar()

for index in range(len(my_list)):
    radio = Radiobutton(ventana, 
                 text=my_list[index], 
                 variable=x, 
                 value=index)
    
    radio.pack()

ventana.mainloop()

