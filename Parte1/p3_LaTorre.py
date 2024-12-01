# Referencias y asignación dinámica en Python
# 2. Implementa una función que cree una matriz, permita llenarla con datos y luego imprima sus elementos.

def matriz(filas, columnas,m):

  for i in range(filas):
    f=[]
    for j in range(columnas):
      a=int(input("|> Elemento "f"[{i}][{j}]: "))
      f.append(a)
    m.append(f)

  j=0
  print("\n| Matriz generada: \n")
  for i in range(filas):
      print(f"{m[j]}")
      j=j+1

print("Generemos una matriz\n")
filas=int(input("|> Número de filas: "))
columnas=int(input("|> Número de columnas: "))

m=[]

matriz(filas,columnas, m)