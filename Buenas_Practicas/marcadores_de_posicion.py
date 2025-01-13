# Autor: Juan Bautista Juárez
# Fecha: Enero de 2024
# Descripción: Buenas prácticas
# Validación de datos de entrada por teclado.
# Conversor a números, enteros y flotantes con validación.
"""
... PARA DEJAR PENDIENTE UNA FUNCIÓN.

"""




def menu()->int:
    """
    Muestra el menú del programa
    :return: Regresa la opción correspondiente a la opción que representa el tipo de acción que se realizara
    """
    print("(1) Convertir a entero ")
    print("(2) Convertir a flotante ")
    print("(0) Salir ")
    seleccion=int(input("Ingrese su opción: "))



def cadena_a_entero(cadena:str) -> int | None:
    """
    Función que convierte la cadena a un entero que está validado.
    :param cadena:  Es la cadena a convertir a número entero.
    :return: La cadena convertida en un entero.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None
def cadena_a_flotante(cadena):
    raise NotImplementedError("Implementar Función")

#Código a nivel de módulo.
opcion=None
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        num_cadena=input("Ingresa el numero a convertir")
        num=cadena_a_entero(num_cadena)
    elif opcion==2:
        num_cadena = input("Ingresa el numero a convertir")
        num = cadena_a_flotante(num_cadena)
        while num in None:
            num_cadena=input("Opción  no valida. Intente nuevamente. ")
            num=cadena_a_entero(num_cadena)
    elif opcion==0:
        print("Programa Terminado")



