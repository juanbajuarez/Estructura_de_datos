# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Juego de piedra, papel o tijeras utilizando
# diccionarios en Python.

"""
Por clave-valor
Ejemplos de usos
nombre_diciionarios={'key':"valor",'key2':"valor2"}
"""
from numpy.random import choice


# Función que asigna los valores del jugador y la CPU.
def jugador(opcion):
    opciones = ["PIEDRA", "PAPEL", "TIJERAS"]
    eleccion_usuario = opciones[opcion - 1]
    eleccion_cpu = choice(["PIEDRA", "PAPEL", "TIJERAS"])
    return eleccion_usuario, eleccion_cpu


# Función del menú.
def menu():
    print("1) PIEDRA")
    print("2) PAPEL")
    print("3) TIJERAS")
    print("0) SALIR")
    opcion = int(input("Ingrese su opcion: "))
    return opcion


# Código a nivel de módulo.
jugador_v = cpu = empate = 0
opcion = None
while opcion != 0:
    print("***  Juego de piedra, papel o tijeras  ***")
    opcion = menu()
    if opcion > 3 or opcion < 0:
        print("Opcion invalida")
    elif opcion == 0:
        print("Programa terminado")
        break
    else:
        diccionario = jugador(opcion)
        print()
        piedra_papel_tijera = {('PIEDRA', 'TIJERAS'): "JUGADOR", ('PIEDRA', 'PAPEL'): "CPU",
                               ('TIJERAS', 'PAPEL'): "JUGADOR", ('TIJERAS', 'PIEDRA'): "CPU",
                               ('PAPEL', 'PIEDRA'): "JUGADOR", ('PAPEL', 'TIJERAS'): "CPU", }

        # Lógica para determinar al ganador.
        resultado = piedra_papel_tijera.get(diccionario)
        if resultado == "JUGADOR":
            print(f"Jugador: {diccionario[0]}. CPU: {diccionario[1]}. "
                  f"El resultado es: Gana del Jugador.")
            jugador_v += 1
        elif resultado == "CPU":
            print(f"Jugador: {diccionario[0]}. CPU: {diccionario[1]}. "
                  f"El resultado es: Gana la CPU.")
            cpu += 1
        else:
            print(f"Jugador: {diccionario[0]}. CPU: {diccionario[1]}. "
                  f"El resultado es: Empate.")
            empate += 1

        print(f"Victorias del jugador: {jugador_v}. Victorias de la CPU: {cpu}. Empates: {empate}.")
