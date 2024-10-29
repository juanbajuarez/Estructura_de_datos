# Juan Bautista Juarez
# 16  de Octubre  de 2024
# Operadores logicos en Python

#Entrada por consola de una cadena

cadena1= input("ingrese si o no: ")
cadena2= input("ingrese si o no: ")
#Conversion de la cadena a minusculas y a un valor booleano
cadena1=cadena1.lower()=="si"
cadena2=cadena2.lower()=="si"
cadena3=bool(cadena1)
cadena4=bool(cadena2)
print(cadena3)
print(cadena4)
#Se aplica el algebra de bool
print(f"¿Ambas fueron si,{cadena3 and cadena4}") #Or devuelve un true si y solo si las dos
# variables son verdaderas.
print(f"¿Ambas fueron iguales,{cadena3 or cadena4}") #Or devuelve un true si al menos una de las dos
# variables es verdaderas.
print(f"¿La negacion de cadena 1,{not cadena3}")#Retorna la negacion de la variable.
print(f"¿La negacion de cadena 2,{not cadena4}")


