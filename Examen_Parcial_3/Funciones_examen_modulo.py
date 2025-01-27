# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Descripción: Exámen tercer parcial.
# Módulo del programa de juegos en python.
import time
import sys
from termcolor import colored

def valida_numeros(cadena:str)->float|None:
    """
    Función que valída que el valor corresponda a un dato del tipo flotante.
    :param cadena: Dato que se comprobara si es un número.
    :return: Si el dato es correcto regresa un flotante y si es incorrecto regresa un None.
    """
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-').replace(".", "")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None
def valida_nombre(cadena:str)->str|None:
    """
    Función que valída que el valor corresponda a un dato del tipo flotante.
    :param cadena: Dato que se comprobara si es un número.
    :return: Si el dato es correcto regresa un flotante y si es incorrecto regresa un None.
    """
    cadena_sin_espacios=cadena.replace(" ", "")
    if cadena_sin_espacios.isalpha():
        return str(cadena)
    else:
        return None

def nombre()->str:
    """

    :return:
    """
    nombre = input("Ingrese su nombre: ")
    nombre = valida_nombre(nombre)
    while nombre is None:
        print("Dato invalido")
        nombre = input("Ingrese un nombre valido: ")
        nombre = valida_nombre(nombre)
    return nombre




def menu_juegos()->int:
    """
    Función que te muestra el menú de los juegos,
    Valída la estrada de datos.
    :param: No recibe ningún valor
    :return: El entero correspondiente a la opción seleccionada.
    """
    print()
    print("***************************")
    print("Menú de juegos disponibles:")
    print("1) Juego de gato")
    print("2) Juego de ahorcados")
    print("3) Conectados")
    print("0) Salir")
    opcion=input("Ingrese el número del juego deseado: ")
    while not (opcion.isnumeric() and 0<=int(opcion)<=3):
        print("Opción no válida")
        print("***************************")
        print("Menú de juegos disponibles:")
        print("1) Juego de gato")
        print("2) Juego de ahorcados")
        print("3) Conectados")
        print("0) Salir")
        opcion=input("ingrese el número del juego deseado: ")
    opcion=int(opcion)
    return opcion


def menu_calculadora()->int:
    """
    Función que te muestra el menú de las operaciones.
    Valída la estrada de datos.
    :param: No recibe ningún valor
    :return: El entero correspondiente a la opción seleccionada.
    """
    print("*************")
    print("Calculadora:")
    print("1) Suma")
    print("2) Multiplicar")
    print("0) Salir")
    opcion=input("Ingrese el número del la operación a realizar: ")
    while not (opcion.isnumeric() and 0<=int(opcion)<=2):
        print("Opción no válida, intente de nuevo. ")
        print("*****************")
        print("Calculadora:")
        print("1) Suma")
        print("2) Multiplicar")
        print("0) Salir")
        opcion = input("Ingrese el número del la operación a realizar: ")

    opcion=int(opcion)
    return opcion

def suma_numeros(num1:float,num2:float)->float:
    """
    Función que suma dos números ya validados
    :param num1: Número a sumar.
    :param num2:Número a sumar.
    :return: La suma de los dos números recibidos.
    """
    return num1+num2
def suma()->None:
    """
     Logica empleada para realizar la suma
    """
    num1 = input("Ingrese el primer número: ")
    num1 = valida_numeros(num1)
    while num1 is None:
        print("Dato invalido")
        num1 = input("Ingrese un número valido: ")
        num1 = valida_numeros(num1)
    num2 = input("Ingrese el segundo número: ")
    num2 = valida_numeros(num2)
    while num2 is None:
        print("Dato invalido")
        num2 = input("Ingrese un número valido: ")
        num2 = valida_numeros(num2)
    print("El resultado de la suma es: ",suma_numeros(num1, num2))

def multiplicacion()->None:
    """
     Logica empleada para realizar la multiplicación
    """
    num1 = input("Ingrese el primer número: ")
    num1 = valida_numeros(num1)
    while num1 is None:
        print("Dato invalido")
        num1 = input("Ingrese un número valido: ")
        num1 = valida_numeros(num1)
    num2 = input("Ingrese el segundo número: ")
    num2 = valida_numeros(num2)
    while num2 is None:
        print("Dato invalido")
        num2 = input("Ingrese un número valido: ")
        num2 = valida_numeros(num2)
    print("El resultado de la multiplicación es: ",multiplica_numeros(num1, num2))

def multiplica_numeros(num1:float,num2:float)->float:
    """
    Función que suma dos números ya validados
    :param num1: Número a sumar.
    :param num2:Número a sumar.
    :return: La suma de los dos números recibidos.
    """
    return num1*num2




def imprimir_titulo_conecta4() -> None:
    """
    Función para imprimir el título del juego conecta 4.
    """
    dibujo = f"""
    {colored('CCCCC   OOOOO   N   N  EEEEE  CCCCC  TTTTT  AAAAA      44', 'red')}
    {colored('C      O     O  NN  N  E      C        T    A   A     4 4', 'cyan')}
    {colored('C      O     O  N N N  EEEE   C        T    AAAAA   44444', 'yellow')}
    {colored('C      O     O  N  NN  E      C        T    A   A       4', 'blue')}
    {colored('CCCCC   OOOOO   N   N  EEEEE  CCCCC    T    A   A       4', 'red')}
    """
    sprint(dibujo,0.01)

def cabeza()->None:
    """
        Función para imprimir el título del juego del ahorcado.
        """
    dibujo = f"""
          {colored('   00000 ', 'red')}
          {colored('   00000' , 'cyan')}
          {colored('     0'   , 'yellow')}
          {colored('  0 000 0', 'blue')}
          {colored('     0   ', 'red')}
          {colored('    0 0 ' , 'red')}
        """
    sprint(dibujo,0.01)
def cuello()->None:
    """
        Función para imprimir el título del juego del ahorcado.
        """
    dibujo = f"""
          {colored('   00000 ', 'red')}
          {colored('   00000' , 'cyan')}
          {colored('     0'   , 'yellow')}
          {colored('         ', 'blue')}
          {colored('         ', 'red')}
          {colored('        ' , 'red')}
        """
    sprint(dibujo,0.01)
def cuerpo()->None:
    """
        Función para imprimir el título del juego del ahorcado.
        """
    dibujo = f"""
          {colored('   00000 ', 'red')}
          {colored('   00000' , 'cyan')}
          {colored('     0'   , 'yellow')}
          {colored('    000  ', 'blue')}
          {colored('     0   ', 'red')}
          {colored('        ' , 'red')}
        """
    sprint(dibujo,0.01)

def mano_i()->None:
    """
        Función para imprimir el título del juego del ahorcado.
        """
    dibujo = f"""
          {colored('   00000  ', 'red')}
          {colored('   00000  ', 'cyan')}
          {colored('     0    ', 'yellow')}
          {colored('    000 0 ', 'blue')}
          {colored('     0    ', 'red')}
          {colored('         ' , 'red')}
        """
    sprint(dibujo,0.01)

