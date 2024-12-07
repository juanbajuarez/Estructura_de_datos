# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Introduccion a diccionarios en Python.

"""
Por clave-valor
Ejemplos de usos
nombre_diciionarios={'key':"valor",'key2':"valor2"}
"""
from Ciclos.Ciclos_ej4_cuenta_bancaria import opcion

PIEDRA="Piedra"
PAPEL="Papel"
TIJERAS="Tijeras"
JUGADOR="Gana el juagador"
EMPATE="Empate"
CPU="Gana la cpu"

#Función del menu
def menu():
    print("1) PIEDRA")
    print("2) PAPEL")
    print("3) TIJERA")
    opcion=int(input("Ingrese su opcion: "))
    return opcion