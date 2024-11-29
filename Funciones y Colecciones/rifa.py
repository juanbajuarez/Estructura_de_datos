"""
1) Ver correos de participantes.

2) Agregar correo de participante.

3) Eliminar correo de participante.

4) Seleccionar ganador.
0) Salir

"""
import random


# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza funciones con listas
# para implementar una lista de compras.

#Función que muestra el menú
def menu():
    print("[1] Ver lista")
    print("[2] Añadir participante")
    print("[3] Eliminar participante")
    print("[4] Seleccionar gandador")
    print("[0] Salir")
    opcion = int(input("Indique qué acción desea realizar: "))
    return opcion

#Función que muestra todos los participantes a la lista.
def lista_participantes(participantes):
    participantes1=set(participantes)
    print("Lista de participantes")
    for participante in participantes1:
        print(participante)
#Función que agrega un participante a la lista.
def agregar_participante(participantes):
    participante = input("Ingrese el nombre del participante: ")
    participantes.append(participante)
    print(f"¡El participante [{participante}] ha sido añadido con éxito!")
    return 1

#Función que elimina un participante de la lista.
def eliminar_participante(participantes):
    lista_participantes(participantes)
    participante = input("Indique el nombre del participante a eliminar: ")
    if participante in participantes:
        participantes.remove(participante)
        print(f"¡El participante: {participante} a sido eliminado correctamente!")
        val=1
    else:
        print(f"¡El participante: {participante} no existe!")
        val=0

    return val

def ganador(participantes):
    participantes_sinrepetir=set(participantes)
    ganador=list(participantes_sinrepetir)
    gandor1 = random.choice(ganador)
    print(gandor1)

#Código a nivel de módulo.
print("*** Lista de participantes ***")
participantes = []
opcion = None
total_p=0
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        if total_p==0:
           print("No hay participantes")
        else:
            lista_participantes(participantes)
    elif opcion == 2:
        total_p+=agregar_participante(participantes)
    elif opcion == 3:
        if total_p==0:
           print("No hay participantes")
        else:
            total_p-=eliminar_participante(participantes)

    elif opcion == 4:
        if total_p==0:
           print("No hay participantes")
        else:
            ganador(participantes)
    elif opcion == 0:
        print("Fin del programa.")
    else:
        print("Opción no válida.")
    print("************************************")









