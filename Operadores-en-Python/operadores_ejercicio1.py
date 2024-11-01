# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Ejercicio número 1 de operadores en Python.

"""
Ejercicio número 1 de operadores en Python. Este programa indica si el usuario es
acreedor a una bonificación siempre y cuando cumpla dos condiciones: que su compra sea mayor o igual
a 5000 y que sea a meses sin intereses.
"""

print("Programa que indica si eres acreedor a una bonificación")

compras = float(input("Ingrese la cantidad gastada en las compras: "))  # Recibe el monto gastado en la compra.
cadena1 = input("¿Las compras fueron a meses sin intereses (sí o no)?: ")  # Indica si es a MSI o no.
cadena1 = cadena1.lower() == "sí"  # Convierte a booleano.

# Evalúa la expresión y muestra si el usuario aplica para la bonificación.
print(f"¿Aplica a bonificación? {cadena1 and compras >= 5000}")
