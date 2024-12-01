#Funciones en Python
# 2. Implementar una función recursiva que calcule el n-ésimo termino de la sucesión de Fibonacci.
def Fibonacci(n):
  if n<0:
    print("| ¡El número seleccionado no es válido!")
  elif n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input("| Buscaremos el n-ésimo término de la sucesión de Fibonacci\n| ¿Qué valor desea hallar?: "))

print("| El número en la posición",n,"es: ",Fibonacci(n-1))
