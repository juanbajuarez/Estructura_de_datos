# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza el ciclo for
# para visualizar distintas formas de pirámides formadas por *
# mediante funciones.

def forma1(tamanio):
    # Pirámide creciente
    print("Forma 1")
    for i in range(1, tamanio + 1):
        print("* " * i)
    print("*************************")

def forma2(tamanio):
    # Pirámide decreciente
    print("Forma 2")
    for i in range(tamanio, 0, -1):
        print("* " * i)
    print("*************************")

def forma3(tamanio):
    # Pirámide centrada
    print("Forma 3")
    for i in range(1, tamanio + 1):
        print(" " * (tamanio - i) + "* " * i)
    print("*************************")

def forma4(tamanio):
    # Pirámide alineada a la derecha
    print("Forma 4")
    for i in range(1, tamanio + 1):
        print("  " * (tamanio - i) + "* " * i)
    print("*************************")

#Código a nivel de módulo.
print("Programa que imprime piramides con asteriscos (*)")
tamanios=int(input("Ingrese el tamaño de la piramide: "))

#Llamada a las funciones, con el tamaño como argumento.
forma1(tamanios)
forma2(tamanios)
forma3(tamanios)
forma4(tamanios)
print()
print("Fin del programa.")