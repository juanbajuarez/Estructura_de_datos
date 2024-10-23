# Juan Bautista Juarez
# 21  de Octubre  de 2024
# Ejercicio número 1 de convesion de valores en Python.

nombre = input("Ingresa el nombre del profesor: ")
no_cubiculo = int(input("Ingresa el no. de cubículo: "))
no_horas = int(input("Ingresa el no. de clases que imparte por semana: "))
antiguedad= input("¿Tiene más de 5 años en la unsij (Si/No)?: ")
antiguedad=antiguedad.lower()=="si"

print(f"El profesor {nombre} se encuentra en el cubiculo número {no_cubiculo} e imparte  {no_horas:.3f} horas de clase a la semana. Además, el tiene más de 5 años en la UNSIJ: {antiguedad}.")

