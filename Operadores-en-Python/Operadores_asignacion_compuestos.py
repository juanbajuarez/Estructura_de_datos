# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Operadores aritméticos compuestos en Python.

"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.)
con el operador de asignación (=).
"""

# Se solicita un número para realizar diferentes operaciones de asignación compuestas.
numero = int(input("Ingresa un número: "))
print(f"Valor ingresado: {numero}")

numero += 20      # Equivale a numero = numero + 20
print(f"Nuevo valor (+20): {numero}")

numero -= 4       # Equivale a numero = numero - 4
print(f"Nuevo valor (-4): {numero}")

numero *= 2       # Equivale a numero = numero * 2
print(f"Nuevo valor (*2): {numero}")

numero /= 5       # Equivale a numero = numero / 5
print(f"Nuevo valor (/5): {numero:.2f}")

# Ejemplo: ¿Qué se obtiene cuando los números ingresados son 8 y 7?
print()
# Solicita números por consola.
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

# Realiza las operaciones utilizando la asignación compuesta.
numero1 += numero2
numero1 += 2
numero1 *= 5
numero2 -= 3
numero1 /= numero2

# Imprime el resultado de las operaciones de asignación compuesta.
print(f"Resultado de las operaciones sobre el primer número: {numero1}")
print(f"Resultado de las operaciones sobre el segundo número: {numero2}")