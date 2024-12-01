# Cadenas en Python
# Escribe un programa que reciba una cadena y cuente cuántas palabras contiene.

def Num_palabras(cadena):
    num_palabras=cadena.split()
    return len(num_palabras)

cadena=input("|> Ingrese una cadena para contar el número de palabras: ")
resultado=Num_palabras(cadena)

print("| El número de palabras que contiene tu cadena es: ",resultado)