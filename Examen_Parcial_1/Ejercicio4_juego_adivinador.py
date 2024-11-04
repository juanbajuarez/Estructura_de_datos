"""
Programa 4 del examen.
"""
from random import randint

print("*** Programa del juego del adivinador ***")
numero = randint(0, 100)
contador = 1

while contador <= 5:
    print(f"Número de intento: {contador}", end=" ")
    intento = int(input("Ingrese un número entre 1 y 100: "))

    if intento > numero:
        print("El número ingresado es mayor al número buscado.")
        contador += 1
    elif intento < numero:
        print("El número ingresado es menor al número buscado.")
        contador += 1
    elif intento == numero:
        print(f"*** ¡Felicidades! Adivinaste en {contador} intentos. ***")
        break

    if contador == 6:
        print(f"*** Perdiste. El número era: {numero}. ***")
