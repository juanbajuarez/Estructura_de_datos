# Juan bautista Juarez
# 29  de octubre  de 2024
#Ciclo while en Python
#Cuenta de banco 1

print("PROGRAMA DE GESTION BANCARIA")
print("*** Bienvenido al Banco azteca ***")

saldo_inicial=1200

opcion=10

while opcion!=0:
    print()
    print("Menú de operaciones")
    print("[1]Consultar saldo")
    print("[2]Ingresar dinero")
    print("[3]Retirar dinero")
    print("[0]Salir")
    opcion=int(input("Opción: "))
    if opcion==1:
        print("Consulta de saldo")
        print(f"Su saldo disponibles es: {saldo_inicial:.2f}")

    elif opcion==2:
        print("Ingreso de dinero")
        abono=float(input("Valor de la cantidad a ingresar: "))
        saldo_inicial+=abono
        print(f"Su saldo actual es {saldo_inicial:.2f}")

    elif opcion == 3:
        print("Retiro de dinero")
        retiro = float(input("Valor de la cantidad a retirar: "))
        if retiro<=saldo_inicial:
            saldo_inicial -= retiro
            print(f"Su saldo actual es {saldo_inicial:.2f}")
        else:
            print("Saldo insuficiente")

    elif opcion == 0:
        print("Programa terminado")
        opcion = 0
    else:
        print("Opción inválida")
