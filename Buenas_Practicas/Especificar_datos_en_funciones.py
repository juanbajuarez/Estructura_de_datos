# Autor: Juan Bautista Juárez
# Fecha: Enero de 2024
# Descripción: Especificar datos en funciónes

def cadena_s_entero(cadena):
    no_guiones=cadena.count("-")
    revisar_cadena=cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None

#Código a nivel de módulo.

num_cadena=input("Ingresa Z: ")
numero=cadena_a_flotante(num_cadena)

while numero is None:
    print("Opción inválida")
    num_cadena = input("Ingresa Z: ")
    numero=cadena_a_flotante(num_cadena)
print(f"EL número {numero} es de tipo {type(numero)}")
