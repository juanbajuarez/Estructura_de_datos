# Juan bautista Juarez
# 28  de octubre  de 2024
# Sentencias de control if  en Python

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

# Ejemplo en donde se imprime un mensaje si el usuario tiene la mayoría de edad.
print("  ***  Programa que determina si eres mayor de edad  ***")
numero = int(input("Ingresa tu edad: "))

if numero >= 18: #Si el numero ingresado es mayor o igual a 18 entrara al ciclo
    print("Eres mayor de edad.")#Intrucciones con un tabulador se consideran intrucciones del if

print("Este código se ejecuta después de evaluarse la sentencia if.")
