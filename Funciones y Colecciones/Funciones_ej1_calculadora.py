# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza funciones y ciclo
# While para implementar una calculadora.


# Declaracion y diseño de las funciones de las operaciones
def menu():
    print()
    print("Menú de operaciones")
    print("[1]Suma")
    print("[2]Resta")
    print("[3]Multiplicación")
    print("[4]División")
    print("[5]División entera")
    print("[6]Exponenciación")
    print("[0]Salir")
    opcion = int(input("Opción: "))
    return opcion

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def division_Entera(a,b):
    return a//b

def exponenciacion(a,b):
    return a**b

#Código a nivel de módulo.
print("*** Calculadora Básica ***")
opcion=None
while opcion!=0:
    opcion=menu()
    if opcion>=1 and opcion<=6:
        x=float(input("Ingrese el primer numero a operar: "))
        y=float(input("Ingrese el segundo numero a operar: "))
    if opcion==1:
        print("El resultado es",suma(x,y))
    elif opcion==2:
        print("El resultado es",resta(x,y))
    elif opcion==3:
        print("El resultado es",multiplicacion(x,y))
    elif opcion==4:
        print("El resultado es",division(x,y))
    elif opcion==5:
        print("El resultado es",division_Entera(x,y))
    elif opcion==6:
        print("El resultado es",exponenciacion(x,y))
    elif opcion>6:
        print("Opción inválida")
    else:
        print("Ciclo terminado")
    print("*************************************")
print("Fin del programa")
