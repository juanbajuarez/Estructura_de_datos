# Autor: Juan Bautista Juárez
# Fecha: Enero de 2024
# Descripción: Buenas prácticas
# Validación de datos de entrada por teclado.
# Conversor a números, enteros y flotantes con validación.
"""
... PARA DEJAR PENDIENTE UNA FUNCIÓN.


"""




def menu()->int:
    pass

def cadena_a_entero(cadena:str) -> int | None:
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
        while numero in None:
            num_cadena=input("Opción  no valida. Intente nuevamente. ")
            numero=cadena_a_entero(num_cadena)
    elif opcion==0:
        print("Programa Terminado")



