def menu() -> int:
    print("1) Sumar")
    print("2) Restar")
    print("0) Salir")
    opcion = int(input("Ingrese su opción:"))
    return opcion

def suma(num1, num2: float) -> float:
    suma = num1 + num2
    return suma

def resta(num1, num2: float) -> float:
    resta = num1 - num2
    return resta
