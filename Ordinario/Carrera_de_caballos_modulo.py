# Autor: Juan Bautista Juárez
# Fecha: febrero de 2025
# Carrera de caballos módulo.
import random
import time

def main():
    """
    Función principal de la carrera de caballos
    :return:
    """
    carrera_caballos()

def eleccion_caballo()->int:
    """
       Función que valida la elección de un caballo.
       :param: No recibe ningún valor
       :return: El entero correspondiente al caballo seleccionado.
       """
    print("***🏇Carrera de caballos🏇***")
    print("[1]Bastos    🐎")
    print("[2]Oro       🐎")
    print("[3]Copas     🐎")
    print("[4]Espadas   🐎")
    apuesta = input("Ingrese el numero de su caballo a seguir o ingrese 0 para finalizar: ")
    while not (apuesta.isnumeric() and 0 <= int(apuesta) <= 2):
        print("Valor no asociado a ningún caballo")
        print("***🏇Carrera de caballos🏇***")
        print("[1]Bastos    🐎")
        print("[2]Oro       🐎")
        print("[3]Copas     🐎")
        print("[4]Espadas   🐎")
        apuesta = input("Ingrese el numero de su caballo a seguir o ingrese 0 para finalizar: ")
    apuesta = int(apuesta)
    return apuesta

def seleccion_cartas_base(cartas_retrocede:list,maso_cartas:list)->list:
    """
    Función que selecciona 6 cartas base
    :param cartas_retrocede: La lista que almacenara las 6 cartas base
    :param maso_cartas: Lista que contiene las 36 cartas de la baraja española.
    :return: La lista con las 6 cartas base para la carrera
    """
    for i in range (6):
        carta=random.choice(maso_cartas)
        cartas_retrocede.append(carta)
        maso_cartas.remove(carta)
    return cartas_retrocede

def carrera_caballos()->None:
    """
    Función que desarrolla la logica para implementar una carrera de caballos
    :return: No regresa ningún valor
    """
    caballo_Oro = """🐎"""
    caballo_Copas = """🐎"""
    caballo_Espadas = """🐎"""
    caballo_Bastos = """🐎"""
    apuesta = eleccion_caballo()
    if apuesta==0:
        print("Simulación de carrera anulada")
    else:
        maso_cartas = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "10B", "11B",
                       "1O", "20", "30", "40", "50", "60", "70", "100", "110",
                       "1C", "2C", "3C", "4C", "5C", "6C", "7C", "10C", "11C",
                       "1E", "2E", "3E", "4E", "5E", "6E", "7E", "10E", "11E"]

        cartas_bastos = ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "10B", "11B"]
        cartas_oro = ["1O", "20", "30", "40", "50", "60", "70", "100", "110"]
        cartas_copas = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "10C", "11C"]
        cartas_espadas = ["1E", "2E", "3E", "4E", "5E", "6E", "7E", "10E", "11E"]
        cartas = [" * ", " * ", " * ", " * ", " * ", "*", ]
        cartas_retrocede = []
        cartas_retrocede = seleccion_cartas_base(cartas_retrocede, maso_cartas)
        print("Cartas:", cartas)
        cbas = ces = cor = cco = 0
        ultimo = 7
        retroceso = 0
        caballo_ganador = 0
        for i in range(30):
            carta = random.choice(maso_cartas)
            print(f"Carta num {i + 1}", carta)
            maso_cartas.remove(carta)
            if carta in cartas_bastos:
                cbas += 7
                print("***🏇Carrera de caballos🏇***")
                print("Bastos    " + " " * cbas + caballo_Bastos)
                print("Oro       " + " " * cor + caballo_Oro)
                print("Copas     " + " " * cco + caballo_Copas)
                print("Espadas   " + " " * ces + caballo_Espadas)
                print("Cartas:", cartas)


            elif carta in cartas_oro:
                cor += 7
                print("***🏇Carrera de caballos🏇***")
                print("Bastos    " + " " * cbas + caballo_Bastos)
                print("Oro       " + " " * cor + caballo_Oro)
                print("Copas     " + " " * cco + caballo_Copas)
                print("Espadas   " + " " * ces + caballo_Espadas)
                print("Cartas:", cartas)
            elif carta in cartas_copas:
                cco += 7
                print("***🏇Carrera de caballos🏇***")
                print("Bastos    " + " " * cbas + caballo_Bastos)
                print("Oro       " + " " * cor + caballo_Oro)
                print("Copas     " + " " * cco + caballo_Copas)
                print("Espadas   " + " " * ces + caballo_Espadas)
                print("Cartas:", cartas)

            else:
                ces += 7
                print("***🏇Carrera de caballos🏇***")
                print("Bastos      " + " " * cbas + caballo_Bastos)
                print("Oro         " + " " * cor + caballo_Oro)
                print("Copas       " + " " * cco + caballo_Copas)
                print("Espadas     " + " " * ces + caballo_Espadas)
                print("Cartas:", cartas)
            time.sleep(2)

            if cbas >= ultimo and cor >= ultimo and cco >= ultimo >= ultimo and ces >= ultimo:
                cartas[retroceso] = cartas_retrocede[retroceso]
                if cartas[retroceso] in cartas_bastos:
                    cbas -= 7
                    print("***🏇Carrera de caballos🏇***")
                    print("Bastos    " + " " * cbas + caballo_Bastos)
                    print("Oro       " + " " * cor + caballo_Oro)
                    print("Copas     " + " " * cco + caballo_Copas)
                    print("Espadas   " + " " * ces + caballo_Espadas)
                    print("Cartas:", cartas)
                elif cartas[retroceso] in cartas_oro:
                    cor -= 7
                    print("***🏇Carrera de caballos🏇***")
                    print("Bastos    " + " " * cbas + caballo_Bastos)
                    print("Oro       " + " " * cor + caballo_Oro)
                    print("Copas     " + " " * cco + caballo_Copas)
                    print("Espadas   " + " " * ces + caballo_Espadas)
                    print("Cartas:", cartas)
                elif cartas[retroceso] in cartas_copas:
                    cco -= 7
                    print("***🏇Carrera de caballos🏇***")
                    print("Bastos    " + " " * cbas + caballo_Bastos)
                    print("Oro       " + " " * cor + caballo_Oro)
                    print("Copas     " + " " * cco + caballo_Copas)
                    print("Espadas   " + " " * ces + caballo_Espadas)
                    print("Cartas:", cartas)
                else:
                    ces -= 7
                    print("***🏇Carrera de caballos🏇***")
                    print("Bastos    " + " " * cbas + caballo_Bastos)
                    print("Oro       " + " " * cor + caballo_Oro)
                    print("Copas     " + " " * cco + caballo_Copas)
                    print("Espadas   " + " " * ces + caballo_Espadas)
                    print("Cartas:", cartas)
                retroceso += 1
                ultimo += 7
        ganador = max(cbas, cor, cco, ces)
        if ganador == cbas:
            print("El caballo ganador es el de Bastos")
            caballo_ganador = 1
        elif ganador == cor:
            print("El caballo ganador es el de Oro")
            caballo_ganador = 2
        elif ganador == cco:
            print("El caballo ganador es el de Copas")
            caballo_ganador = 3
        else:
            print("El caballo ganador es el de Espadas")
            caballo_ganador = 4
        if apuesta == caballo_ganador:
            print("Tu caballo ah ganado la carrera")
        else:
            print("Tu caballo ha perdido la carrera")