def MostrarDatos(estudiante):
    print("datos del estudiante: ")
    print("nombre: ", estudiante["nombre"])
    print("Promedio: ", estudiante["Promedio"])
    print("Edad: ", estudiante["Edad"])

estudiante = {"nombre":"FLAVIO", "Edad":19 , "Promedio":13.34}

MostrarDatos(estudiante)

