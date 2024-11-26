# Juan bautista Juarez
# 25  de octubre  de 2024
# Calculadora con funciones


#Declaracion y diseño de las funciones
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

#Programa pricipal

print("*** Calculadora Básica ***")
opcion=None
while opcion!=0:
    menu()
    opcion=int(input("Opción: "))
    if opcion==0:
        print("Opción inválida", end="\n")
        break
    x=float(input("Ingrese el primer numero a operar: "))
    y=float(input("Ingrese el segundo numero a operar:"))
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

    print("*************************************")
print("Fin del programa")
