# Estructuras en python
#  2. Implementar un programa que permita representar la información de un estudiante: su nombre, edad y promedio. Además, implemente una función función para mostrar los detalles del estudiante.
def MostrarDatos(estudiante):
    print("datos del estudiante: ")
    print("nombre: ", estudiante["nombre"])
    print("Promedio: ", estudiante["Promedio"])
    print("Edad: ", estudiante["Edad"])

estudiante = {"nombre":"FLAVIO", "Edad":19 , "Promedio":13.34}

MostrarDatos(estudiante)

"""
Python ofrece un sintaxis más permisiva en este caso con los diccionarios, que nos permiten relacionar pares elementos (clave: valor) 
que pueden ser de tipos heterogeneos, y ademas es mutable(puedes cambiar un valor, o agregar un par "clave:valor"). 

En C++ tendriamos que crear un tipo de dato definido por el usuario (estructura), definir los diferentes tipos de dato que va almacenar, 
crea un variable y asignarle los valores correspondientes, y al final utilizar el operador punto para acceder a los datos e imprimirlos.

"""