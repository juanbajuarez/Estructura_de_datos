# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Ejercicios tercer parcial.
# Módulo del programa que suma todos los números pares.

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


def suma_pares(*vargs)->None:
    """
    Función que suma todos los números pares.
    :param vargs:Lista de todos los números ingresados por el usuario.

    """
    suma = 0
    for var in vargs:
        if var %2==0:
            suma+=var
    print("La suma de los números pares es: ",suma)


def main() -> None:

    """
    Función principal del programa.
    """
    lis_num = []
    num_cadena = input(f"Ingresa un número [{len(lis_num) + 1}] o presiona enter para finalizar: ")
    while bool(num_cadena):
        numero = cadena_a_entero(cadena=num_cadena)
        if numero is None:
            print("Formato no válido, intenta nuevamente.")

        else:
            lis_num.append(numero)
        num_cadena = input(f"Ingresa un número [{len(lis_num) + 1}] o presiona enter para finalizar: ")
    suma_pares(*lis_num)