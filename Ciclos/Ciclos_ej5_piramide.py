# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza el ciclo while y for
# para visualizar distintas formas de pirámides formadas por *.

print("Programa que imprime pirámides con asteriscos (*)")
tamanio = int(input("Ingrese el tamaño de la pirámide: "))

# Validación del tamaño de la pirámide.
if tamanio <= 0:
    print("Error: El tamaño debe ser un número mayor a 0.")
else:
    # Pirámide creciente
    print("Forma 1")
    for i in range(1, tamanio + 1):
        print("* " * i)
    print("*************************")

    # Pirámide decreciente
    print("Forma 2")
    for i in range(tamanio, 0, -1):
        print("* " * i)
    print("*************************")

    # Pirámide centrada
    print("Forma 3")
    for i in range(1, tamanio + 1):
        print(" " * (tamanio - i) + "* " * i)
    print("*************************")

    # Pirámide alineada a la derecha
    print("Forma 4")
    for i in range(1, tamanio + 1):
        print("  " * (tamanio - i) + "* " * i)
    print("*************************")

print("Fin del programa.")

