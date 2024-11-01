import math
print("*** Programa que calcula area y perimetro ***")

opcion=10

while opcion!=0:
    print()
    print("Menú de operaciones")
    print("[1]Área de un rectángulo")
    print("[2]Perimetro de un rectángulo")
    print("[3]Área de un círculo")
    print("[4]Perimetro de un círculo")
    print("[0]Salir")
    opcion=int(input("Opción:"))
    if opcion==1:
        print("Área de un rectángulo")
        numero1=float(input("Ingrese la base del rectangulo: "))
        numero2 = float(input("Ingrese la altura del rectangulo: "))
        area_rectangulo=numero1*numero2
        print(f"EL área del rectangulo es: {area_rectangulo:.3f}")
    elif opcion==2:
        print("Perimetro de un rectángulo")
        numero1 = float(input("Ingrese la base del rectangulo: "))
        numero2 = float(input("Ingrese la altura del rectangulo: "))
        perimetro_rectangulo=2*numero1+2*numero2
        print(f"El perimetro del rectangulo: {perimetro_rectangulo:.3f}")
    elif opcion==3:
        print("Área de un círculo")
        numero1=float(input("Ingrese el radio del circulo: "))
        area_circulo= math.pi*numero1**2
        print(f"El área de un circulo es: {area_circulo:.3f}")
    elif opcion==4:
        print("Perimetro de un círculo")
        numero1 = float(input("Ingrese el radio del circulo: "))
        perimetro_circulo = math.pi * numero1 * 2
        print(f"El perimetro de un circulo es: {perimetro_circulo:.3f}")
    elif opcion==0:
        print("Programa terminado")
        opcion =0
    else:
        print("Opción inválida")
    print("*******************************")
