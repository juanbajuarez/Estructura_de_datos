# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Juego de piedra, papel, tijeras, lagarto y spock utilizando
# diccionarios en Python.

"""
Por clave-valor
Ejemplos de usos
nombre_diciionarios={'key':"valor",'key2':"valor2"}
"""
from numpy.random import choice

# Función que asigna los valores del jugador y la CPU.
def jugador(opcion):
    opciones = ["PIEDRA", "PAPEL", "TIJERAS","LAGARTO","SPOCK"]
    eleccion_usuario = opciones[opcion - 1]
    eleccion_cpu = choice(["PIEDRA", "PAPEL", "TIJERAS","LAGARTO","SPOCK"])
    return eleccion_usuario, eleccion_cpu


# Función del menú.
def menu():
    print("1) PIEDRA")
    print("2) PAPEL")
    print("3) TIJERAS")
    print("4) LAGARTO")
    print("5) SPOCK")
    print("6) REGLAS")
    print("0) SALIR")
    opcion = int(input("Ingrese su opción: "))
    return opcion

#Función que muestra las reglas
def reglas():
    print("Reglas:")
    print("Selecciona una opción de acuerdo a lo siguente:")
    print("-Tíjeras cortan papel.")
    print("-Papel cubre piedra.")
    print("-Piedra aplasta lagarto.")
    print("-Lagarto envenena spock.")
    print("-Spock destrulle tíjeras.")
    print("-Tíjeras decapitan lagarto.")
    print("-Lagarto come papel.")
    print("-Papel desaprueba spock.")
    print("-Spock vaporiza piedra.")
    print("-Piedra aplasta tíjera.")
    print("La CPU una de las opciones de manera aleatoria.")
    print("___________________________________________________")
    print()

# Código a nivel de módulo.
jugador_v = cpu = empate = 0
opcion = None
while opcion != 0:
    print("***  Juego de piedra, papel o tijeras  ***")
    opcion = menu()
    if opcion > 6 or opcion < 0:
        print("Opción invalida")
    elif opcion == 0:
        print("Programa terminado")
        break
    elif opcion== 6:
        reglas()
    else:
        seleccion = jugador(opcion)
        print()
        # Declaración del diccionario
        piedra_papel_tijera_lagarto_spock = {('TIJERAS','PAPEL'): "JUGADOR", ('PAPEL', 'PIEDRA'): "JUGADOR",
                               ('PIEDRA', 'LAGARTO'): "JUGADOR", ('LAGARTO', 'SPOCK'): "JUGADOR",
                               ('SPOCK', 'TIJERAS'): "JUGADOR", ('TIJERAS','LAGARTO'): "JUGADOR",
                               ('LAGARTO','PAPEL'): "JUGADOR", ('PAPEL','SPOCK'):"JUGADOR",
                               ('SPOCK','PIEDRA'):"JUGADOR",('PIEDRA','TIJERAS'):"JUGADOR",
                               #Casos donde gana la CPU.
                               ('PAPEL','TIJERAS'): "CPU", ('PIEDRA','PAPEL'): "CPU",
                               ('LAGARTO','PIEDRA'): "CPU", ('SPOCK','LAGARTO'): "CPU",
                               ('TIJERAS','SPOCK'): "CPU", ('LAGARTO','TIJERAS'): "CPU",
                               ('PAPEL','LAGARTO'): "CPU", ('SPOCK','PAPEL'): "CPU",
                               ('PIEDRA','SPOCK'): "CPU", ('TIJERAS','PIEDRA', ): "CPU"
                                             }

        # Lógica para determinar al ganador.
        resultado = piedra_papel_tijera_lagarto_spock.get(seleccion)
        if resultado == "JUGADOR":
            print(f"Jugador: {seleccion[0]}. CPU: {seleccion[1]}. "
                  f"El resultado es: Gana del Jugador.")
            jugador_v += 1
        elif resultado == "CPU":
            print(f"Jugador: {seleccion[0]}. CPU: {seleccion[1]}. "
                  f"El resultado es: Gana la CPU.")
            cpu += 1
        else:
            print(f"Jugador: {seleccion[0]}. CPU: {seleccion[1]}. "
                  f"El resultado es: Empate.")
            empate += 1

        print(f"Victorias del jugador: {jugador_v}. Victorias de la CPU: {cpu}. Empates: {empate}.")
