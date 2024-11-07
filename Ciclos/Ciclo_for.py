# Juan bautista Juarez
# 6 de noviembre  de 2024
#Ciclo for en Python


"""
sintaxis
for variable in secuencias:

"""
cadena_de_usuario=input("Ingrese una cadena:")
contador=0
for caracter in cadena_de_usuario:
    contador+=1
    print(f"{caracter}",end=" - ")
print()
print(contador)

alumnos=["Rosalinda","Juan","Lourdes","Tania","Bryan","Rebeca","Jennifer","Hector","Galilea","Patricia","Jesus","Addi"]

for alumno in alumnos:
    print(f"Hola {alumno}")

for i in range(1,10):
    print(f"{i}",end=", ")