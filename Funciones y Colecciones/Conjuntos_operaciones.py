# Juan bautista Juarez
# 25 de noviembre  de 2024
# Conjuntos en Python
"""


"""
import random

conjunto_A={11,7,10,9,5,1,15,7}
conjunto_B={55,70,11,77,66,9,5}
print(conjunto_A)
print(conjunto_B)

#Union
union=conjunto_A|conjunto_B
print(union)

#Interseccion
interseccion=conjunto_A & conjunto_B
print(interseccion)

#diferencia A-B
diferencia=conjunto_A - conjunto_B
print(diferencia)

#diferencia B-A
diferencia2=conjunto_B - conjunto_A
print(diferencia2)

#Lista de animales
lista_animales=["aguila","conejo","leopardo","ballena","tigre","aguila"]
print("Lista original: ",lista_animales)
conjunto_animales=set(lista_animales)
print("Conjunto: ",conjunto_animales)
lista_modificada=list(conjunto_animales)
print("Lista modificada",lista_modificada)
tupla_animales=tuple(lista_modificada)
print("Tupla: ",tupla_animales)

expone=["anarquistas","ctrlz"]
gandor=random.choice(expone)
print(gandor)
