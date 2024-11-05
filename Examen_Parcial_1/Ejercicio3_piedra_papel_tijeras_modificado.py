"""
Programa 3 del examen modificado.
"""
import random

opcion = 1
jugador = 0
empate = 0
cpu_victorias = 0

while opcion != "0":
    print("*** Juego de Piedra, Papel o Tijera ***")
    numero = random.randint(1, 3)
    print()
    print(f"Victorias del jugador: {jugador}, Empates: {empate}, Victorias del CPU: {cpu_victorias}")
    print("Elije Piedra, Papel ó Tijera")
    print("[0] Salir")
    opcion=(input("Opción: "))
    opcion=opcion.lower()

    if numero == 1:
        la_cpu = "piedra"
    elif numero == 2:
        la_cpu = "papel"
    else:
        la_cpu = "tijera"

    print()

    # Casos de empate
    if opcion == "piedra" and la_cpu == "piedra":
        print(f"Jugador: piedra, CPU: {la_cpu}. El resultado es Empate")
        empate += 1
    elif opcion == "papel" and la_cpu == "papel":
        print(f"Jugador: papel, CPU: {la_cpu}. El resultado es Empate")
        empate += 1
    elif opcion == "tijera" and la_cpu == "tijera":
        print(f"Jugador: tijera, CPU: {la_cpu}. El resultado es Empate")
        empate += 1

    # Casos donde gana el jugador
    elif opcion == "piedra" and la_cpu == "papel":
        print(f"Jugador: piedra, CPU: {la_cpu}. El ganador es el jugador")
        jugador += 1
    elif opcion == "papel" and la_cpu == "tijera":
        print(f"Jugador: papel, CPU: {la_cpu}. El ganador es el jugador")
        jugador += 1
    elif opcion == "tijera" and la_cpu == "piedra":
        print(f"Jugador: tijera, CPU: {la_cpu}. El ganador es el jugador")
        jugador += 1

    # Casos donde gana la cpu
    elif opcion == "piedra" and la_cpu == "tijera":
        print(f"Jugador: piedra, CPU: {la_cpu}. El ganador es la cpu")
        cpu_victorias += 1
    elif opcion == "papel" and la_cpu == "piedra":
        print(f"Jugador: papel, CPU: {la_cpu}. El ganador es la cpu")
        cpu_victorias += 1
    elif opcion == "tijera" and la_cpu == "papel":
        print(f"Jugador: tijera, CPU: {la_cpu}. El ganador es la cpu")
        cpu_victorias += 1

    elif opcion == "0":
        print("Programa terminado")
        break
    else:
        print("Opción inválida")

    print("*******************************")
