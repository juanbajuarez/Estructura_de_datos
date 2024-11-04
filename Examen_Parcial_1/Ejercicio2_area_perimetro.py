"""
Programa 2 del examen.
"""
import math
print("*** Programa que calcula área y perímetro ***")

opcion = 10

while opcion != 0:
    print()
    print("Menú de operaciones")
    print("[1] Área de un rectángulo")
    print("[2] Perímetro de un rectángulo")
    print("[3] Área de un círculo")
    print("[4] Perímetro de un círculo")
    print("[0] Salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        print("Área de un rectángulo")
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area_rectangulo = base * altura
        print(f"El área del rectángulo es: {area_rectangulo:.3f}")

    elif opcion == 2:
        print("Perímetro de un rectángulo")
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        perimetro_rectangulo = 2 * (base + altura)
        print(f"El perímetro del rectángulo es: {perimetro_rectangulo:.3f}")

    elif opcion == 3:
        print("Área de un círculo")
        radio = float(input("Ingrese el radio del círculo: "))
        area_circulo = math.pi * radio ** 2
        print(f"El área del círculo es: {area_circulo:.3f}")

    elif opcion == 4:
        print("Perímetro de un círculo")
        radio = float(input("Ingrese el radio del círculo: "))
        perimetro_circulo = 2 * math.pi * radio
        print(f"El perímetro del círculo es: {perimetro_circulo:.3f}")

    elif opcion == 0:
        print("Programa terminado")

    else:
        print("Opción inválida")

    print("*******************************")

