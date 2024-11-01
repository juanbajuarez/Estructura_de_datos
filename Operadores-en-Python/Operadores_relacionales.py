# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Operadores relacionales en Python.

"""
Los operadores relacionales son símbolos que se utilizan en programación para comparar dos valores.
Estos operadores devuelven un valor booleano (verdadero o falso) dependiendo del resultado de la comparación.
Son fundamentales para tomar decisiones dentro de un programa, ya que permiten construir expresiones condicionales
que determinan el flujo de ejecución.

Operadores Relacionales Comunes:
Operador    Significado
==          Igual a
!=          Diferente de
>           Mayor que
<           Menor que
>=          Mayor o igual que
<=          Menor o igual que
"""

# Se solicitan dos números flotantes para realizar distintas operaciones relacionales.
numero1 = float(input("Ingresa un número decimal: "))
numero2 = float(input("Ingresa otro número decimal: "))

print()

# Las siguientes relaciones devuelven un valor booleano (True o False).
# Pregunta si los dos números son iguales.
print(f"¿Los números son iguales? {numero1 == numero2}")

# Pregunta si los números son diferentes.
print(f"¿Los números son diferentes? {numero1 != numero2}")

# Pregunta si el primer número es mayor que el segundo.
print(f"¿El número {numero1:.2f} es mayor que {numero2:.2f}? {numero1 > numero2}")

# Pregunta si el primer número es menor que el segundo.
print(f"¿El número {numero1:.2f} es menor que {numero2:.2f}? {numero1 < numero2}")

# Pregunta si el primer número es mayor o igual que el segundo.
print(f"¿El número {numero1:.2f} es mayor o igual que {numero2:.2f}? {numero1 >= numero2}")

# Pregunta si el primer número es menor o igual que el segundo.
print(f"¿El número {numero1:.2f} es menor o igual que {numero2:.2f}? {numero1 <= numero2}")
