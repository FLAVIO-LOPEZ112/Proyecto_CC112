#Archivos en Python
#2. Escribir datos en un archivo de texto

with open("Parte1\datos1.txt", "w") as archivo:
    archivo.write("Lopez\nOcampo\nFlavio\nRaul")
    print("se agregaron los datos correctamente")

"""
archivo = open("Parte1\datos1.txt", "w")
archivo.write("Lopez\nOcampo\nFlavio\nRaul")
print("se agregaron los datos correctamente")
archivo.close()
"""
"""
Python nos ofrece manipular archivos sin necesdidad de librerias adicionales, ademas nos brinda funciones que abren y cierran el 
archivo de forma automatica(como se muestra en el comentario anterior). En C++ necesitamos mas pasos para realizar esta tarea, lo
que hace que el codigo sea menos leible, pero ofrece un mejor control sobre el manejo de los archivos que Python. 
"""