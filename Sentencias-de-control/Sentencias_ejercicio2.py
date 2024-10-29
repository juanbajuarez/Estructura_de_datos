# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Programa para determinar la estación del año a partir del mes.

print("*** Programa que determina la estación del año ***")
mes = int(input("Ingresa el número del mes: "))

# Utiliza la sentencia if-elif-else
# Se imprimirá la estación del año según el número que se ingrese
if 3 <= mes <= 5:
    print("Primavera.")
elif 6 <= mes <= 8:
    print("Verano.")
elif 9 <= mes <= 11:
    print("Otoño.")
elif mes == 12 or mes == 1 or mes == 2:
    print("Invierno.")
else:
    print("Mes incorrecto.")
