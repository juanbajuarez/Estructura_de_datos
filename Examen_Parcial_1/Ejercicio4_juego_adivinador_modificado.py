"""
Programa 4 del examen modificado.
"""
from optparse import Option
from random import randint


print("*** Programa del juego del adivinador ***")
print("Elige la dificultad del juego")
print("[F] Facil")
print("[M] Medio")
print("[D] Dificil")

opcion_dificultad=(input("Ingrese su opcion: "))
opcion_dificultad=opcion_dificultad.lower()

if opcion_dificultad=="f":
    numero = randint(1, 50)
    contador = 1
    print(numero) #Linea para tener numero visible para pruebas
    while contador <= 10:
        print(f"Número de intento: {contador}", end=" ")
        intento = int(input("Ingrese un número entre 1 y 50: "))

        if intento > numero:
            print("El número ingresado es mayor al número buscado.")
            contador += 1
        elif intento < numero:
            print("El número ingresado es menor al número buscado.")
            contador += 1
        elif intento == numero:
            print(f"*** ¡Felicidades! Adivinaste en {contador} intentos. ***")
            break

        if contador == 11:
            print(f"*** Perdiste. El número era: {numero}. ***")


elif opcion_dificultad == "m":
    numero = randint(1, 100)
    contador = 1
    print(numero)#Linea para tener numero visible para pruebas
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

elif opcion_dificultad == "d":
    numero = randint(1, 110)
    contador = 1
    print(numero)#Linea para tener numero visible para pruebas
    while contador <= 4:
        print(f"Número de intento: {contador}", end=" ")
        intento = int(input("Ingrese un número entre 1 y 110: "))

        if intento > numero:
            print("El número ingresado es mayor al número buscado.")
            contador += 1
        elif intento < numero:
            print("El número ingresado es menor al número buscado.")
            contador += 1
        elif intento == numero:
            print(f"*** ¡Felicidades! Adivinaste en {contador} intentos. ***")
            break

        if contador == 5:
            print(f"*** Perdiste. El número era: {numero}. ***")
