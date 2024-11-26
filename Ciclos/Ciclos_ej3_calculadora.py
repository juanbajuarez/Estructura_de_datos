# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza el ciclo while para
# la implementación de una calculadora.

print("*** Calculadora Básica ***")

opcion=None
while opcion!=0:
    #Despliega el menú de opciones de la calculadora.
    print()
    print("Menú de operaciones")
    print("[1]Suma")
    print("[2]Resta")
    print("[3]Multiplicación")
    print("[4]División")
    print("[5]División entera")
    print("[6]Exponenciación")
    print("[0]Salir")
    opcion=int(input("Opción: "))
    # Se realizará la operación que sea seleccionada.
    if opcion==1:
        print("Suma")
        numero1=float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        suma=numero1+numero2
        print(f"La suma es: {suma:.2f}")
    elif opcion==2:
        print("Resta")
        numero1=float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resta=numero1-numero2
        print(f"La resta es: {resta:.2f}")
    elif opcion==3:
        print("Multiplicación")
        numero1=float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        producto= numero1 * numero2
        print(f"El producto es: {producto:.2f}")
    elif opcion==4:
        print("División")
        numero1=float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        division = numero1 / numero2
        print(f"División es: {division:.2f}")
    elif opcion==5:
        print("División entera")
        numero1=float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        divisionE = numero1 // numero2
        print(f"La división entera es: {divisionE}")
    elif opcion==6:
        print("Exponenciación")
        numero1=float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        exponenciacion = numero1 ** numero2
        print(f"La exponenciación es: {exponenciacion:.2f}")
    #Si se ingresa cualquier otro número se considera inválido.
    else:
        print("Opción inválida")
print("Fin del programa.")