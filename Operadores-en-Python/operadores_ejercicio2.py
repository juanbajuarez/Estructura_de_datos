# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Ejercicio número 2 de operadores en Python.

"""
Este programa indica si el usuario forma
parte de la comunidad UNSIJ, ya sea como profesor o estudiante.
"""

# Entrada de datos.
cadena1 = input("¿Es profesor de la UNSIJ? (sí o no): ")
cadena2 = input("¿Es estudiante de la UNSIJ? (sí o no): ")

# Conversión a minúsculas y luego a booleanos.
cadena1 = cadena1.lower() == "sí"
cadena2 = cadena2.lower() == "sí"

# Será verdadero si al menos una de las condiciones es verdadera.
print(f"¿Forma parte de la comunidad de la UNSIJ? {cadena1 or cadena2}")
