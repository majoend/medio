
#atributos ----> son las caracteristicas
#metodos -----> son las acciones que hacen

class Animal():
    def dormir(self):
        print('Este animal esta durmiendo')
#creo que estoy entendiendo las instancias, es para poder usar la clase creo
animal = Animal()

#quiero llamar a los metodos, osea lo que esta dentro de esa clase en la funcion 
animal.dormir()

#creo que asi ya funciona
#luego quisiera crear mas clases e iria haciendo lo mismo


#Ahora creare unas clases que hereden, y hereden a ver como quedan luego

class Seres(): #esta seria la clase principal
    vivos = True

class Personas(Seres): #esta clase hereda a la primera
    def caminar(self):
        print('Las personas caminan')

class Hijas(Personas): #luego hijas pasó a heredar de personas
    def estudiar(self):
        print('Las hijas estudian')

vivas = Seres()
personas = Personas()
hijas = Hijas()

personas.caminar()
hijas.estudiar()

#-----------------------------
# CREAMOS UNA CLASE
class Auto():

#PASAMOS LOS METODOS A USAR
    def encender(self):
        print('El auto esta encendido')
        return self

    def conducir(self):
        print('Estas conduciendo un auto')
        return self
    
    def frenar(self):
        print('Frenaste el auto')
        return self

auto = Auto() #EN LUGAR DE PONER TANTAS LINEAS DE CODIGO, LO HACEMOS DE ESTA FORMA

auto.encender().conducir().frenar() #ASI ENCADENAMOS LOS METODOS




