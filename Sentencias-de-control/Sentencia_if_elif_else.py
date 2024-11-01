# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Sentencias de control if-elif-else en Python.

"""
La sentencia elif es una extensión del if-else que permite evaluar múltiples condiciones de forma secuencial.
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición
que sea verdadera.

Sintaxis:

if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.

elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
"""

# Ejemplo que determina el grupo al que pertenece una persona de acuerdo a su edad.
print("  ***  Programa que determina el grupo de acuerdo a la edad  ***")
edad = int(input("Ingresa tu edad: "))

# Lógica para determinar el grupo usando la estructura if-elif-else.
# Solo se ejecutará el bloque de código donde se cumpla la condición.
if edad < 14:
    grupo = "Niños y adolescentes"
elif 15 <= edad < 25:
    grupo = "Jóvenes"
elif 25 <= edad < 45:
    grupo = "Adultos jóvenes"
elif 45 <= edad < 60:
    grupo = "Adultos maduros"
else:
    grupo = "Adultos mayores"

# Se imprimirá el valor asignado al grupo según la condición que se cumplió.
print(f"El grupo al que perteneces es: {grupo}.")
