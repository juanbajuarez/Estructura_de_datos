# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Exámen ejercicio número 1 "Escaleras" modificado.

#Función del menú.
def menu():
    print("***  Ejercicio 1. La escalera.  ***")
    opcion=int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:"))
    return opcion

#Funcion para la escalera creciente.
def escalera_creciente(tam):
    print("  " * (tam+1), "_")
    print("  " * tam,"_|")
    for i in range((tam-1),-1,-1):
        print("  " * i, "_|")
    print("__"*(tam+2))

#Funcion para la escalera decreciente.
def escalera_decreciente(tam):
    print("_")
    print(" |_")
    for i in range(1, tam+1):
        print("  " * i, "|_")
    print("__"*(tam+1))

# Código a nivel de módulo.
escalera = None
while escalera != 0:
    escalera = menu()
    if escalera >0:
        escalera_decreciente(escalera)
    elif escalera < 0:
        escalera_creciente(-escalera)
    else:
        print("Programa Terminado")
