# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Exámen ejercicio número 1 "Escaleras"

#Función del menú.
def menu():
    print("***  Ejercicio 1. La escalera.  ***")
    opcion=int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:"))
    return opcion

#Funcion para la escalera creciente.
def escalera_creciente(tam):
    print("  " * tam,"_")
    for i in range((tam-1),-1,-1):
        print("  " * i, "_|")
    print("__"*(tam+1))

#Funcion para la escalera decreciente.
def escale_decreciente(tam):
    print("_")
    for i in range(0, tam):
        print("  " * i, "|_")
    print("__"*(tam+1))

# Código a nivel de módulo.
escalera = None
while escalera != 0:
    escalera = menu()
    if escalera >0:
        escalera_creciente(escalera)
    elif escalera < 0:
        escale_decreciente(-escalera)
    else:
        print("Programa Terminado")
