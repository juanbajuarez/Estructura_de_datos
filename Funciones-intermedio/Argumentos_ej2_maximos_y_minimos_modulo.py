# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Ejercicios tercer parcial.
# Módulo del programa que encuentra el menor y mayor de los números ingresados por consola.

def cadena_a_flotante(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """

    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None



def min_mayor(*vargs)->None:
    """
    Encuentra el número minimo y el máximo de la lista.
    :param vargs:Lista de todos los números ingresados por el usuario.

    """
    minimo=may=vargs[0]
    for var in vargs:
        if var>may:
            may=var
        if var<minimo:
            minimo=var

    print("El  número menor es: ",minimo)
    print("El  número mayor es: ",may)


def main() -> None:

    """
    Función principal del programa.

    """
    lis_num = []
    num_cadena = input(f"Ingresa el número [{len(lis_num) + 1}] o presiona enter para finalizar: ")
    while bool(num_cadena):
        numero = cadena_a_flotante(cadena=num_cadena)
        if numero is None:
            print("Dato no válido, intenta nuevamente.")

        else:
            lis_num.append(numero)
        num_cadena = input(f"Ingresa el número [{len(lis_num) + 1}] o presiona enter para finalizar: ")
    min_mayor(*lis_num)