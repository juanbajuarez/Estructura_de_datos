# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Sentencias de control if-else en Python.

"""
La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera.

else:
    # Código a ejecutar si la condición es falsa.

# Código que se ejecuta sin importar la condición.
"""

# Ejemplo en donde se determina si un número es par o impar.
print("  ***  Programa que determina si un número es par o impar  ***")
numero = int(input("Ingresa un número: "))  # Solicitamos un número entero

# Lógica para determinar si el número ingresado es par o impar.
print()
if numero % 2 == 0:  # Condición que implica que el número es par.
    print("El número es par.")
else:
    print("El número es impar.")  # Condición que implica que el número es impar.