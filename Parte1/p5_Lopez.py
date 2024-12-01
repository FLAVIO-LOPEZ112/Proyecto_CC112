
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