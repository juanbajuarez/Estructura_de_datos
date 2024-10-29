# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Sentencias de control if en Python.

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulación.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

# Ejemplo en donde se imprime un mensaje si el usuario tiene la mayoría de edad.
print("  ***  Programa que determina si eres mayor de edad  ***")
numero = int(input("Ingresa tu edad: "))

if numero >= 18:  # Si el número ingresado es mayor o igual a 18, se ejecutará el bloque de código.
    print("Eres mayor de edad.")  # Instrucciones con tabulación, consideradas dentro del if.

print("Este código se ejecuta después de evaluarse la sentencia if.")