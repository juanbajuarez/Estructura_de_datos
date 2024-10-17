# Juan bautista Juarez
# 16  de octubre  de 2024
# Se utilizan para comparar dos valor en Python

cadena1= input("ingrese si o no: ")
cadena2= input("ingrese si o no: ")
cadena1=cadena1.lower()=="si"
cadena2=cadena2.lower()=="si"
cadena3=bool(cadena1)
cadena4=bool(cadena2)
print(cadena3)
print(cadena4)
print(f"¿Ambas fueron si,{cadena3 and cadena4}")
print(f"¿Ambas fueron iguales,{cadena3 or cadena4}")
print(f"¿La negacion de cadena 1,{not cadena3}")
print(f"¿La negacion de cadena 2,{not cadena4}")


