

from tkinter import *

def submit():
    print('La temperatura es:', str(barra.get()) + ' grados')
window = Tk()

barra = Scale(window, from_=0, to=100, 
              orient=HORIZONTAL,
               tickinterval=10, 
               length=500,)
barra.pack()


window.title('Scale Example')
window.geometry('500x500')

radio = Button(window, text='Send',
                command=submit)
radio.pack()


window.mainloop()