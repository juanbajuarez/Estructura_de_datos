# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Ejercicios tercer parcial.
# Módulo del programa que calcula el factorial de un número.

def factorial(n: int) -> int:
    """
    Función recursiva que calcula el factorial de un número.
    :param n: Número entero no negativo.
    :return: Factorial del número ingresado.
    """
    # El caso base, por definición el factorial de 0 es 1.
    if n == 0 or n == 1:
        return 1
    #Caso recursivo, busca un número menor.
    return n * factorial(n - 1)

def cadena_a_entero(cadena: str) -> int | None:
    """
    Función que convierte una cadena a un número entero.
    :param cadena: Cadena a convertir.
    :return: Regresa el número entero si cumple con el formato, en caso contrario, devuelve None.
    """
    if cadena.isnumeric():
        return int(cadena)
    else:
        return None

def main() -> None:

    """
    Función principal del programa.
    """
    num= input(f"Ingresa un número entre 0 y un entero positivo:")
    numero = cadena_a_entero(cadena=num)
    if numero is None:
        print("Formato no válido.")
        print("Fin del programa.")

    else:
        print(factorial(numero))