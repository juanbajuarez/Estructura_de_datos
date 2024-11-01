# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Programa para determinar el promedio de una materia y si aprobó o no.

print("*** Programa para calcular el promedio de una materia ***")

# Solicita las calificaciones de parciales y ordinario
calificacion1 = float(input("Ingresa la calificación del parcial 1: "))
calificacion2 = float(input("Ingresa la calificación del parcial 2: "))
calificacion3 = float(input("Ingresa la calificación del parcial 3: "))
ordinario = float(input("Ingresa la calificación del ordinario: "))

# Calcula el promedio.
promedio = ((calificacion1 + calificacion2 + calificacion3)/6 + ordinario/2)
# Muestra el promedio con un decimal.
print(f"La calificación final es: {promedio:.1f}.", end=" ")

# Sentencia if-else para decir si aprobó o no la materia
if promedio >= 6.0:
    print("¡Felicidades! Aprobaste.")
else:
    print("Lo siento, no aprobaste.")
