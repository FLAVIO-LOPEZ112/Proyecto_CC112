# Clases en Python 
# 1. Definir una clase Persona con atributos nombre y edad, y un método para mostrar estos datos. 

class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
    
    def MostrarDatos(self):
        print("*Datos de la Persona*")
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)

persona1 = Persona("Julio", 25)
persona1.MostrarDatos()

"""
Python destaca en la creaccion rapida de clases, sin la necesidad el uso de constructores ni destructores explicitos. Pero a pesar de
que en C++ se tendria que escribir el codigo de una forma más explicita, esto ofrece un mayor control y presción.  
"""