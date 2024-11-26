# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza el ciclo while para
# la implementación de una cuenta bancaria.

print("PROGRAMA DE GESTIÓN BANCARIA")
print("*** Bienvenido a tu cuenta de Banco azteca ***")

saldo_inicial=0
opcion=None
while opcion!=0:
    # Despliega el menú de movimientos del Banco.
    print()
    print("Menú de operaciones")
    print("[1] Consultar saldo")
    print("[2] Ingresar dinero")
    print("[3] Retirar dinero")
    print("[0] Salir")
    opcion=int(input("Opción: "))
    # Se realizará el movimiento que sea seleccionada.

    # Consulta saldo.
    if opcion==1:
        print("Consulta de saldo")
        print(f"Su saldo disponibles es: {saldo_inicial:.2f}")

    # Ingresar dinero a la cuenta.
    elif opcion==2:
        print("Ingreso de dinero")
        abono=float(input("Valor de la cantidad a ingresar: "))
        saldo_inicial+=abono
        print(f"Su saldo actual es {saldo_inicial:.2f}")
    # Retirar dinero de la cuenta.

    elif opcion == 3:
        print("Retiro de dinero")
        retiro = float(input("Valor de la cantidad a retirar: "))
        if retiro<=saldo_inicial:
            saldo_inicial -= retiro
            print(f"Su saldo actual es {saldo_inicial:.2f}")
        else:
            print("Saldo insuficiente")

    #Finaliza el programa.
    elif opcion == 0:
        print("Ciclo terminado")
    else:
        print("Opción inválida")
print("Fin del programa.")