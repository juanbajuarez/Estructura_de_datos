# Juan bautista Juarez
# 21  de octubre  de 2024
# Sentencias de control en if-else Python

#if condicion:
# Condicon a ejecutar si
# la condicion es verdad

#else:
# codigo que se ejecuta si el if no es verdad

print("Programa que determina si un numero es par o impar")
numero=input("Ingrese un numero: ")
numero=int(numero)
if numero%2==0:
    print(f"En numero {numero} es par")
else:
    print(f"En numero {numero} es impar")