# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Operadores aritméticos en Python.

"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""

# Se solicitan dos números enteros al usuario.
numero1 = int(input("Ingresa un número entero: "))
numero2 = int(input("Ingresa otro número entero: "))

# Se realizan las operaciones aritméticas.
print()
print("  ***   Ejemplos de uso de los operadores aritméticos   ***")

# Expresión de suma dentro del print, dándole formato (f) al código de impresión.
print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}.")

# Expresión de resta dentro del print, dándole formato (f) al código de impresión.
print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}.")

# Expresión de multiplicación dentro del print, dándole formato (f) al código de impresión.
print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}.")

# Expresión de división dentro del print, dándole formato (f) al código de impresión.
print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}.")    # Notar la forma para mostrar dos decimales.

# Expresión de división entera dentro del print, dándole formato (f) al código de impresión.
print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}.")

# Expresión del módulo dentro del print, dándole formato (f) al código de impresión.
print(f"El módulo de ({numero1} % {numero2}) es: {numero1 % numero2}.")

# Expresión de exponenciación dentro del print, dándole formato (f) al código de impresión.
print(f"La exponenciación de ({numero1} ** {numero2}) es: {numero1 ** numero2}.")