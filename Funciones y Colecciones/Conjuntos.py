# Juan bautista Juarez
# 25 de noviembre  de 2024
# Conjuntos en Python
"""
desordenados
inmutables
Ejemplo de uso de los conjuntos
lista[]
tuplas()
conjuntos y diccionarios {}
"""

print("***************************************************************")
print("Ejemplo de uso de los conjuntos")
conjunto_nombre=set() #{} se utiliza para diccionarios, se crea un conjunto vacio

#Conjunto inicial
print("Conjunto vacio:",conjunto_nombre)

#Se añaden valores al conjunto
conjunto_nombre.add("Jamilet")
conjunto_nombre.add("Bryan")
conjunto_nombre.add("Juan")
conjunto_nombre.add("Rebeca")
conjunto_nombre.add("Jesus")
conjunto_nombre.add("Tania")
conjunto_nombre.add("Marlene")
conjunto_nombre.add("Linda")
conjunto_nombre.add("Galilea")
conjunto_nombre.add("Alberto")
conjunto_nombre.add("Ady")
conjunto_nombre.add("Patricia")

print("Conjunto 303:",conjunto_nombre)

#Anadir elementos repetidos
print("Añadiendo elementos repetidos")
conjunto_nombre.add("Juan")
print("Conjunto 303 actualizado:",conjunto_nombre)

#Eliminar elementos
conjunto_nombre.remove("Jesus")
print("Conjunto 303 actualizado:",conjunto_nombre)

#Mostrar todos los elementos
for nombre in conjunto_nombre:
    print(nombre,end=",")
print()
#verifica si un elemento pertence a un conjunto
print(f"¿El elemento Juan pertenece al conjunto?",{"Juan" in conjunto_nombre})
print(f"¿El elemento Jesus pertenece al conjunto?",{"Jesus" in conjunto_nombre})
print()

#Nuevo conjunto de numeros
conjunto_numeros=set()
conjunto_numeros.add(12.5)
conjunto_numeros.add(3.5)
conjunto_numeros.add(0.5)
conjunto_numeros.add(54.5)
conjunto_numeros.add(10.5)
print(conjunto_numeros)

#Funciones basicas:

#tamaño del conjunto
print(len(conjunto_numeros))

#suma de los elementos
print(sum(conjunto_numeros))