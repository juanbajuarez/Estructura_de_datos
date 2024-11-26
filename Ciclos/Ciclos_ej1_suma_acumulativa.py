# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza el ciclo while para calcular
# la suma acumulativa de un número ingresado por el usuario hasta 0.

print("Programa que hace una suma acumulativa")

# Solicita al usuario el número final de la suma acumulativa.
num_final = final= int(input("Ingrese el número final: "))
acumulador = 0

# Verifica si el número ingresado es diferente de 0.
if num_final == 0:
    print("Número inválido.")
else:
    # Ciclo que realiza la suma acumulativa desde 0 hasta el número ingresado.
    while num_final != 0:
        acumulador += num_final
        num_final -= 1

    # Muestra el resultado de la suma acumulativa.
    print(f"La suma acumulada desde 0 hasta {final} es: {acumulador}")
print("Fin del programa.")