# Juan Bautista Juárez.
# 17 de octubre de 2024.
# Ejercicio número 4 de operadores en Python.
# Este programa analizará valores booleanos y dirá si la expresión se cumple
# según los datos de entrada.

print("Programa que evalúa valores booleanos.")

# Solicitud de entrada de valores de v (verdadero) o f (falso).
expresion1 = input("Ingrese el valor de expresión 1 (V/F): ")
expresion2 = input("Ingrese el valor de expresión 2 (V/F): ")
expresion3 = input("Ingrese el valor de expresión 3 (V/F): ")
expresion4 = input("Ingrese el valor de expresión 4 (V/F): ")

# Conversión a minúsculas y obtención del valor booleano.
expresion1 = expresion1.lower() == "v"
expresion2 = expresion2.lower() == "v"
expresion3 = expresion3.lower() == "v"
expresion4 = expresion4.lower() == "v"

# Evaluación de la expresión.
resultado = (expresion1 or expresion2) and (expresion3 or expresion4)

# Impresión en pantalla del resultado.
print("¿El resultado de la expresión booleana es?", resultado)
