# Estructuras en python
#  2. Implementar un programa que permita representar la información de un estudiante: su nombre, edad y promedio. Además, implemente una función función para mostrar los detalles del estudiante.
def MostrarDatos(estudiante):
    print("datos del estudiante: ")
    print("nombre: ", estudiante["nombre"])
    print("Promedio: ", estudiante["Promedio"])
    print("Edad: ", estudiante["Edad"])

estudiante = {"nombre":"FLAVIO", "Edad":19 , "Promedio":13.34}

MostrarDatos(estudiante)

