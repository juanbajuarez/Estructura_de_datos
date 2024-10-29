# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Operadores lógicos en Python.

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar
decisiones más sofisticadas dentro de nuestros programas.
"""

# Se solicita por consola que se ingresen dos valores (Si/No) para convertirlos en expresiones booleanas.
expresion1 = input("Ingresa un valor (Si/No): ")
expresion2 = input("Ingresa otro valor (Si/No): ")

# Las cadenas se convierten a expresiones booleanas.
expresion1 = expresion1.lower() == "si"
expresion2 = expresion2.lower() == "si"

# Se imprimen mensajes sobre operaciones lógicas.

# Imprime "True" si ambas expresiones son verdaderas.
print(f"¿Ambas expresiones fueron 'sí'? {expresion1 and expresion2}")

# Imprime "True" si al menos una de las expresiones es verdadera.
print(f"¿Alguna expresión fue 'sí'? {expresion1 or expresion2}")

# Imprime lo contrario al valor lógico de la expresión dada.
print(f"Lo contrario de la primera expresión es: {not expresion1}")
print(f"Lo contrario de la segunda expresión es: {not expresion2}")
