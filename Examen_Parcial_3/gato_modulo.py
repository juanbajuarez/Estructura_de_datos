import time
import sys
from termcolor import colored
def juego_del_gato()->None:
    from gato_modulo import usuario_vs_usuario, usuario_vs_cpu
    from gato_modulo import modos_juego
    modo=modos_juego()
    if modo==1:
        usuario_vs_usuario()
    elif modo==2:
        usuario_vs_cpu()
    else:
        print("Saliendo del juego")
print()


def modos_juego()->int:
    """
       Función que te muestra el menú de los juegos,
       Valída la estrada de datos.
       :param: No recibe ningún valor
       :return: El entero correspondiente a la opción seleccionada.
       """
    print()
    print("***************************")
    print("Modo de juego:")
    print("1) Usuario vs Usuarios")
    print("2) Usuario vs CPU")
    print("0) Salir")
    opcion = input("Ingrese el modo de juego: ")
    while not (opcion.isnumeric() and 0 <= int(opcion) <= 2):
        print("Opción no válida")
        print("***************************")
        print("Modo de juego:")
        print("1) Usuario vs Usuarios")
        print("2) Usuario vs CPU")
        print("0) Salir")
        opcion = input("Ingrese el modo de juego: ")
    opcion = int(opcion)
    return opcion

def usuario_vs_usuario()->None:
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Mostrar el tablero inicial
    for i, fila in enumerate(tablero):
        print(" | ".join(fila))
        if i < len(tablero) - 1:
            print("-" * 9)

    # Configuración inicial de los jugadores
    jugadores = ["X", "O"]
    turno_actual = 0  # Comienza el jugador X
    turnos_totales = 0  # Contador de turnos válidos
    juego_terminado = 1
    # Mientras no se hayan jugado los 5 turnos válidos
    while turnos_totales < 9:
        print(f"\nTurno {turnos_totales + 1}: Juega el jugador {jugadores[turno_actual]}")
        try:
            fila = int(input("Ingrese el número de la fila (1-3): "))
            columna = int(input("Ingrese el número de la columna (1-3): "))

            # Validar si las entradas están en rango
            if 1 <= fila <= 3 and 1 <= columna <= 3:
                if tablero[fila - 1][columna - 1] == " ":
                    tablero[fila - 1][columna - 1] = jugadores[turno_actual]
                    turno_actual = 1 - turno_actual  # Cambiar al otro jugador
                    turnos_totales += 1  # Contar el turno como válido
                else:
                    print("Espacio ocupado. Intente nuevamente.")
            else:
                print("Entrada fuera de rango. Por favor ingrese números entre 1 y 3.")
        except ValueError:
            print("Por favor ingrese valores numéricos válidos.")

        if turnos_totales >= 5:
            for fila in tablero:
                if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                    if fila[0] == "X":
                        print("Gano el jugador X")
                    else:
                        print("Gano el jugador O")
                    juego_terminado = 0

                # Comprobar columnas
            for col in range(3):
                if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                    if tablero[0][col] == "X":
                        print("Gano el jugador X")
                    else:
                        print("Gano el jugador O")
                    juego_terminado = 0

                # Comprobar diagonales
            if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
                if tablero[0][0] == "X":
                    print("Gano el jugador X")
                else:
                    print("Gano el jugador O")
                juego_terminado = 0
            if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
                if tablero[0][2] == "X":
                    print("Gano el jugador X")
                else:
                    print("Gano el jugador O")
                juego_terminado = 0

        # Mostrar el tablero actualizado después de cada intento
        for i, fila in enumerate(tablero):
            print(" | ".join(fila))
            if i < len(tablero) - 1:
                print("-" * 9)
        if juego_terminado == 0:
            break
        if turnos_totales==9:
            print("Empate")

def usuario_vs_cpu()->None:
    import random

    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Mostrar el tablero inicial
    for i, fila in enumerate(tablero):
        print(" | ".join(fila))
        if i < len(tablero) - 1:
            print("-" * 9)

    # Configuración inicial
    jugador = "X"  # Usuario
    cpu = "O"  # CPU
    turno_actual = 0  # 0 para el usuario, 1 para la CPU
    turnos_totales = 0  # Contador de turnos válidos
    juego_terminado = 1

    # Mientras no haya un ganador y queden turnos
    while turnos_totales < 9:
        print(f"\nTurno {turnos_totales + 1}: ", end="")

        if turno_actual == 0:  # Turno del usuario
            print("Juega el usuario (X)")
            try:
                fila = int(input("Ingrese el número de la fila (1-3): "))
                columna = int(input("Ingrese el número de la columna (1-3): "))

                # Validar si las entradas están en rango
                if 1 <= fila <= 3 and 1 <= columna <= 3:
                    if tablero[fila - 1][columna - 1] == " ":
                        tablero[fila - 1][columna - 1] = jugador
                        turno_actual = 1  # Cambiar al turno de la CPU
                        turnos_totales += 1  # Contar el turno como válido
                    else:
                        print("Espacio ocupado. Intente nuevamente.")
                else:
                    print("Entrada fuera de rango. Por favor ingrese números entre 1 y 3.")
            except ValueError:
                print("Por favor ingrese valores numéricos válidos.")

        else:  # Turno de la CPU
            print("Juega la CPU (O)")
            while True:
                fila = random.randint(0, 2)
                columna = random.randint(0, 2)
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = cpu
                    turno_actual = 0  # Cambiar al turno del usuario
                    turnos_totales += 1  # Contar el turno como válido
                    break

        # Verificar si hay un ganador
        if turnos_totales >= 5:
            for fila in tablero:
                if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                    if fila[0] == "X":
                        print("Gano el jugador X")
                    else:
                        print("Gano la CPU")
                    juego_terminado = 0

                # Comprobar columnas
            for col in range(3):
                if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                    if tablero[0][col] == "X":
                        print("Gano el jugador X")
                    else:
                        print("Gano la CPU")
                    juego_terminado = 0

                # Comprobar diagonales
            if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
                if tablero[0][0] == "X":
                    print("Gano el jugador X")
                else:
                    print("Gano la CPU")
                juego_terminado = 0
            if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
                if tablero[0][2] == "X":
                    print("Gano el jugador X")
                else:
                    print("Gano la CPU")
                juego_terminado = 0

        # Mostrar el tablero actualizado después de cada intento
        for i, fila in enumerate(tablero):
            print(" | ".join(fila))
            if i < len(tablero) - 1:
                print("-" * 9)

        # Resultado final si no hay ganador
        if juego_terminado == 0:
            break
        elif turnos_totales == 9:
            print("Empate")

def imprimir_titulo_gato()->None:
    """
    Función para imprimir el título del juego del gato.
    """
    dibujo = f"""
    {colored('GGGGG  AAAAA   TTTTT   OOOOO', 'red')}
    {colored('G      A   A     T    O     O', 'cyan')}
    {colored('G  GG  AAAAA     T    O     O', 'yellow')}
    {colored('G   G  A   A     T    O     O', 'blue')}
    {colored('GGGGG  A   A     T     OOOOO', 'red')}
    """
    sprint(dibujo,0.01)

def sprint(text:str, second:float)->None:
    """
    :param text:El título de juego a desplegar.
    :param second: El tiempo de retardo entre cada carácter.
    :return: No retorna ningún valor.
    """
    for line in text:
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(second)

