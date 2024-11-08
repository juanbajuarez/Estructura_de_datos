# Juan bautista Juarez
# 6 de noviembre  de 2024
#Ciclo for en Python


"""
sintaxis del ciclo for
for variable in secuencias:


Programa que imprime una lista de nombres
"""
cadena_de_usuario=input("Ingrese una cadena:")
contador=0

#Ciclo for que cuenta el numero de caracteres de una cadena ingresada y lo imprime
for caracter in cadena_de_usuario:
    contador+=1
    print(f"{caracter}",end=" - ")
print()
print(contador)
#declaracion de una lista de nmbres
alumnos=["Rosalinda","Juan","Lourdes","Tania","Bryan","Rebeca","Jennifer","Hector","Galilea","Patricia","Jesus","Addi"]
#Impreme hola y el nombre del alumno
for alumno in alumnos:
    print(f"Hola {alumno}")

for i in range(1,10):
    print(f"{i}",end=", ")