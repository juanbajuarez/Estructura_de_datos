# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza el ciclo while para calcular
# la suma acumulativa entre dos números ingresados por el usuario.

# Programa que realiza una suma acumulativa entre dos números ingresados por el usuario
print("Programa que hace una suma acumulativa entre dos números")

# Solicita al usuario los números inicial y final.
num_inicial = int(input("Ingrese el número inicial: "))
num_final = final= int(input("Ingrese el número final: "))

# Variable para almacenar el valor acumulado.
acumulador = 0

# Verifica que el número final sea mayor o igual al inicial.
if num_final < num_inicial:
    print("Error: El número final debe ser mayor o igual al número inicial.")
else:
    # Ciclo que realiza la suma acumulativa desde num_final hasta num_inicial.
    while num_final >= num_inicial:
        acumulador += num_final
        num_final -= 1

    # Imprime el resultado de la suma acumulada.
    print(f"La suma acumulada entre {num_inicial} y {final} es: {acumulador}")
print("Fin del programa.")