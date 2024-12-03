# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza funciones con listas
# conjuntos y tuplas para implementar un juego sin repetir valores.
# Autor: Juan Bautista Juárez

#Menú de juego
print(f"            ***  Juego sin repetir  ***")
print("Este es un juego que se puede jugar de manera grupal,",end=" \n")
print("en donde el objetivo es decir palabras de un tema en ",end=" \n")
print("específico y los jugadores deben tratar de no repetir ",end=" \n")
print("la misma palabra. ",end=" \n")

#Funcion que valida si una palabra es repetida o no.
def busca_repetido(palabra_nueva,palabras_ingresadas):
    if palabra_nueva in palabras_ingresadas:
        val=1
    else:
        palabras_ingresadas.append(palabra_nueva)
        val=0
    return val

#Código a nivel de módulo.
categoria=input("Ingrese  el tema de juego: ")
palabras_ingresadas=[]
repetido=None
cantidad_palabras=1

#Ciclo while que termina al repetir una palabra dentro de la categoria
while repetido!=1:
    palabra_nueva=input(f"palabra {cantidad_palabras} del tema {categoria}: ")
    repetido=busca_repetido(palabra_nueva,palabras_ingresadas)
    if repetido==1:
        cantidad_palabras-=1
        print(f"¡Programa terminado!: Han sido {cantidad_palabras} palabras diferentes." )
        print(palabras_ingresadas)
    else:
        cantidad_palabras+=1
print()
print("Fin del programa")

