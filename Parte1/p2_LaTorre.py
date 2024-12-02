# Cadenas en Python
# Escribe un programa que reciba una cadena y cuente cuántas palabras contiene.

def Num_palabras(cadena):
    num_palabras=cadena.split()
    return len(num_palabras)

cadena=input("|> Ingrese una cadena para contar el número de palabras: ")
resultado=Num_palabras(cadena)

print("| El número de palabras que contiene tu cadena es: ",resultado)

"""
Python simplifica mucho la manipulación de cadenas, gracias a sus métodos integrados como split().En C++, dividir cadenas requiere 
usar stringstream para separar palabras basadas en espacios u otros delimitadores, además, que el usuario pueda ingresar una cadena
completa requeriria el uso de getline() y para contar las palabras se necesitaria iterar explicitamente sobre el flujo de palabras.
"""