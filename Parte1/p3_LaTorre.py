# Referencias y asignación dinámica en Python
# 2. Implementa una función que cree una matriz, permita llenarla con datos y luego imprima sus elementos.

def matriz(filas, columnas,m):

  for i in range(filas):
    f=[]
    for j in range(columnas):
      a=int(input("|> Elemento "f"[{i}][{j}]: "))
      f.append(a)
    m.append(f)

  print("\n| Matriz generada: \n")
  for i in range(filas):
      print(f"{m[i]}")
      

print("Generemos una matriz\n")
filas=int(input("|> Número de filas: "))
columnas=int(input("|> Número de columnas: "))

m=[]

matriz(filas,columnas, m)

"""
Las listas en Python son dinámicas, por lo que no es necesario declarar su tamaño inicial ni reservar memoria manualmente como en c++. 
El uso de los bucles for tambien es más automatico(tiene una sintaxis mas sencilla) que en c++, ademas el uso de input() hace que la
iteraccion del usuario sea más sencilla de implementar.
"""