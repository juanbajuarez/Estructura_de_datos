# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Programa para determinar el menor de dos números o si son iguales.

print("*** Programa para determinar el menor de dos números o si son iguales ***")

# Se ingresan dos números de tipo flotante.
numero1 = float(input("Ingresa el primer número decimal: "))
numero2 = float(input("Ingresa el segundo número decimal: "))

# Utiliza la sentencia if-elif-else
if numero1 == numero2:
    print("Ambos números son iguales.")
elif numero2 < numero1:
    print(f"El número {numero2} es menor que {numero1}.")
else:
    print(f"El número {numero1} es menor que {numero2}.")
