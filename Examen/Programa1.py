"""
Programa 1 del examen
"""

from random import *
numero=randint(0, 100)
contador=1
print(numero)
while contador<=5:
    intento=int(input("Ingrese un numero: "))
    if intento>numero:
        print("EL numero ingresado es mayor al numero buscado")
        contador+=1
    elif intento<numero:
        print("EL numero ingresado es menor al numero buscado")
        contador += 1
    elif intento==numero:
        print("*** Felicidades ***")
        print("Adivinaste el numero")
        contador =100
    else:
        print()
    if contador==6:
        print("*** Numero no adivinado ***")
