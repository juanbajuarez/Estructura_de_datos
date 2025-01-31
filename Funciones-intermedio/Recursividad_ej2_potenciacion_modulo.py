# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Ejercicios tercer parcial.
# Módulo del programa que calcula a^b.

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
def potenciacion(a:int,b:int)->int:
    """
    Función para calcular la potencia de un número de manera recursiva.
    :param a: Representa la base de la potencia.
    :param b: Representa el exponente al que será elevado el número
    :return: a elevado a la b.
    """
    #Caso base
    if b==0:
        return 1
    else:
    #Caso recursivo
        #Notar que: a^b = a*(a^(b-1)).
        return a*potenciacion(a,b-1)

def main() -> None:

    """
    Función principal del programa.
    """
    a=input("Ingresa la base a:")
    b=input("Ingresa el exponente b :")
    a_validado=cadena_a_entero(a)
    b_validado=cadena_a_entero(b)
    if a_validado is None or b_validado is None:
        print("Formato invalido")
    else:
        if a_validado==0 and b_validado==0:
            print("0^0=Indeterminado")
        else:
            print((f"{a_validado}^{b_validado}= "),potenciacion(a_validado,b_validado))
    print("Fin del programa")