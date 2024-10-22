# Juan Bautista Juarez
# 21  de Octubre  de 2024
# Entrada de datos por consola para interactuar con el usuario con valores dinámicos.

# Comentar sobre la función input.
#la palabra reservada input indica que el valor que se le asignara a la variable sera entrada por consola.
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")
#Esta instruccion concatena las dos cadenas
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}") #Imprime un numero despues del otro (concatenación).

# Comentar por qué se realiza el casting de variables.
# Convierte la cadena a flotantes
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
#Operacion de aritmetica con flotantes (suma.)
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")#Imprime el resultado de la suma de numeros flotantes