import random
# Autor: Juan Bautista Juárez
# Fecha: Enero de 2024
# Descripción: Juego de piedra, papel o tijeras utilizando
# diccionarios en Python.


from random import choice
# Función que asigna los valores del jugador y la CPU.


def jugador(opciones):
    valores = ["PIEDRA", "PAPEL", "TIJERAS"]
    elecciones_usuario.append(valores[opciones[0] - 1])
    elecciones_usuario.append(valores[opciones[1] - 1])
    elecciones_CPU.append(choice(["PIEDRA", "PAPEL", "TIJERAS"]))
    elecciones_CPU.append(choice(["PIEDRA", "PAPEL", "TIJERAS"]))

# Función del menú.
def menu():
    print("1) JUGAR")
    print("2) SALIR")
    opcion = int(input("Ingrese su opción: "))
    return opcion

# Función del menú.
def submenu():
    print("1) PIEDRA")
    print("2) PAPEL")
    print("3) TIJERAS")
    m_derecha = int(input("Ingrese la opción para su mano derecha: "))
    m_izquierda = int(input("Ingrese la opción para su mano izquierda: "))
    return m_derecha,m_izquierda


# Código a nivel de módulo.
jugador_v = cpu = empate = 0
opcion = None
while opcion != 0:
    elecciones_CPU = []
    elecciones_usuario = []
    print("***  Juego de piedra, papel o tijeras  ***")
    opcion = menu()
    if 0 < opcion > 2:
        print("Opción invalida")
    elif opcion == 2:
        print("Programa terminado")
        break
    else:
        seleccion_usuario_CPU=[]
        opciones=submenu()
        jugador(opciones)
        print(f"Mano derecha: {elecciones_usuario[0]} y mano izquierda: {elecciones_usuario[1]}")
        print("Elecciones de la CPU",elecciones_CPU)
        eleccion_final=int(input("Elige tu mano derecha(1) o tu mano izquierda (2): "))
        seleccion_usuario_CPU=(elecciones_usuario[eleccion_final - 1], random.choice(elecciones_CPU))
        # Declaración del diccionario.
        piedra_papel_tijera = {('PIEDRA', 'TIJERAS'): "JUGADOR", ('PIEDRA', 'PAPEL'): "CPU",
                               ('TIJERAS', 'PAPEL'): "JUGADOR", ('TIJERAS', 'PIEDRA'): "CPU",
                               ('PAPEL', 'PIEDRA'): "JUGADOR", ('PAPEL', 'TIJERAS'): "CPU", }

        # Lógica para determinar al ganador.
        resultado = piedra_papel_tijera.get(seleccion_usuario_CPU)
        if resultado == "JUGADOR":
            print(f"Jugador: {seleccion_usuario_CPU[0]}. CPU: {seleccion_usuario_CPU[1]}. "
                  f"El resultado es: Gana del Jugador.")
            jugador_v += 1
        elif resultado == "CPU":
            print(f"Jugador: {seleccion_usuario_CPU[0]}. CPU: {seleccion_usuario_CPU[1]}. "
                  f"El resultado es: Gana la CPU.")
            cpu += 1
        else:
            print(f"Jugador: {seleccion_usuario_CPU[0]}. CPU: {seleccion_usuario_CPU[1]}. "
                  f"El resultado es: Empate.")
            empate += 1

        print(f"Victorias del jugador: {jugador_v}. Victorias de la CPU: {cpu}. Empates: {empate}.")
        print("****************************************************************************************")
