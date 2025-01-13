# Autor: Juan Bautista Juárez
# Fecha: Enero de 2024
# Descripción: Buenas prácticas
# Validación de datos de entrada por teclado.


#prueba_numero=int(input("Ingrese un numero "))
#print(prueba_numero)

"""
cadena=input("Ingrese una cadena: ").strip()
print(cadena.isnumeric())
print(cadena.isalpha())
print(cadena.isalnum())
"""

numero=input("Ingresa una cadena: ")
while not numero.isnumeric():
    print("Opción Inválida")
    numero=input("Intenta  nuevamente: ")
print()
numero=int(numero)
print(f"EL número {numero} es de tipo {type(numero)}")

def cadena_a_flotante(cadena):
    no_guiones=cadena.count("-")
    no_puntos=cadena.count(".")
    revisar_cadena=cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in(0,1) and no_puntos in(0,1):
        return float(cadena)
    else:
        return None

#Función a nivel de módulo

num_cadena=input("Ingresa Z: ")
numero=cadena_a_flotante(num_cadena)

while numero is None:
    print("Opción inválida")
    num_cadena = input("Ingresa Z: ")
    numero=cadena_a_flotante(num_cadena)
print(f"EL número {numero} es de tipo {type(numero)}")
