# Juan bautista Juarez
# 17  de octubre  de 2024
# Ejercicios de operadores

#Es profesor de la unsij
#Es estudiante
#forma parte de la comunidad unsij


cadena1= input("Es profesor de la unsij si o no: ")
cadena2= input("Es estudiante de la unsij si o no: ")
cadena1=cadena1.lower()=="si"
cadena2=cadena2.lower()=="si"
cadena1=bool(cadena1)
cadena2=bool(cadena2)
print(f"¿Forma parte de la comunidad de unsij? {cadena1 or cadena2}")