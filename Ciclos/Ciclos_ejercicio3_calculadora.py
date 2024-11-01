# Juan bautista Juarez
# 29  de octubre  de 2024
#Ciclo while en Python
#Calculadora en Python 1

print("*** Calculadora Básica ***")

opcion=10
while opcion!=0:
    print()
    print("Menú de operaciones")
    print("[1]Suma")
    print("[2]Resta")
    print("[3]Multiplicación")
    print("[4]División")
    print("[5]División entera")
    print("[6]Exponenciación")
    print("[0]Salir")
    opcion=int(input("Opción:"))
    if opcion==1:
        print("Suma")
        numero1=float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        suma=numero1+numero2
        print(f"La suma es: {suma:.2f}")
    elif opcion==2:
        print("Resta")
        numero1=float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        resta=numero1-numero2
        print(f"La resta es: {resta:.2f}")
    elif opcion==3:
        print("Multiplicación")
        numero1=float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        producto= numero1 * numero2
        print(f"El producto es: {producto:.2f}")
    elif opcion==4:
        print("División")
        numero1=float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        division = numero1 / numero2
        print(f"División es: {division:.2f}")
    elif opcion==5:
        print("División entera")
        numero1=float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        divisionE = numero1 // numero2
        print(f"La división entera es: {divisionE}")
    elif opcion==6:
        print("Exponenciación")
        numero1=float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        exponenciacion = numero1 ** numero2
        print(f"La exponenciación es: {exponenciacion:.2f}")
    elif opcion==0:
        print("Programa terminado")
        opcion =0
    else:
        print("Opción inválida")
