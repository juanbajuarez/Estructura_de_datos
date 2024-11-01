
import random

numero=random.randint(1,3)
print(numero)
print("*** Juego de piedra,papel o tijera ***")

opcion=10
jugador=0
empate=0
cpu_victorias=0
while opcion!=0:
    numero = random.randint(1, 3)
    print()
    print(f"victorias del jugador:{jugador}, empate: {empate} y victorias del CPU: {cpu_victorias} ")
    print("[1]Piedra")
    print("[2]Papel")
    print("[3]Tijera")
    print("[0]Salir")
    opcion_jugador = int(input("Opción:"))
    if numero==1:
        la_cpu="piedra"
    elif numero==2:
        la_cpu="papel"
    elif numero==3:
        la_cpu="tijera"
    print()
    if opcion_jugador==1 and la_cpu=="piedra":
        print(f"Jugador: piedra, CPU: {la_cpu}. EL resultado es Empate")
        empate+=1
    elif opcion_jugador==2 and la_cpu=="papel":
        print(f"Jugador: papel, CPU: {la_cpu}. EL resultado es Empate")
        empate += 1
    elif opcion_jugador==3 and la_cpu=="tijera":
        print(f"Jugador: tijera, CPU: {la_cpu}. EL resultado es Empate")
        empate += 1

    elif opcion_jugador==1 and la_cpu=="papel":
        print(f"Jugador: piedra, CPU: {la_cpu}. EL ganador es la CPU")
        cpu_victorias += 1
    elif opcion_jugador == 1 and la_cpu == "tijera":
        print(f"Jugador: piedra, CPU: {la_cpu}. EL ganador es el jugador")
        jugador+=1

    elif opcion_jugador==2 and la_cpu=="piedra":
        print(f"Jugador: papel, CPU: {la_cpu}. EL ganador es el jugador")
        jugador+=1
    elif opcion_jugador==2 and la_cpu=="tijera":
        print(f"Jugador: papel, CPU: {la_cpu}. EL ganador es la CPU")
        cpu_victorias += 1

    elif opcion_jugador==3 and la_cpu=="piedra":
        print(f"Jugador: tijera, CPU: {la_cpu}. EL ganador es la CPU")
        cpu_victorias += 1
    elif opcion_jugador==3 and la_cpu=="papel":
        print(f"Jugador: tijera, CPU: {la_cpu}. EL ganador es el jugador")
        jugador+=1

    elif opcion==0:
        print("Programa terminado")
        opcion =0
    else:
        print("Opción inválida")
    print("*******************************")
