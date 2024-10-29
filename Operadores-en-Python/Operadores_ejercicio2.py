# Juan Bautista Juarez
# 17  de Octubre  de 2024
# Ejercicio número 2 de operadores en Python. Este programa indica si el usuario forma
# parte de la comunidad UNSIJ, ya sea un profesor o un estudiante.

cadena1= input("Es profesor de la unsij si o no: ")
cadena2= input("Es estudiante de la unsij si o no: ")
cadena1=cadena1.lower()=="si"
cadena2=cadena2.lower()=="si"
cadena1=bool(cadena1)
cadena2=bool(cadena2)
print(f"¿Forma parte de la comunidad de unsij? {cadena1 or cadena2}") #Sera verdadero cuando al menos
# uno sea verdad.