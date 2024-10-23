# Juan bautista Juarez
# 21  de octubre  de 2024
# Sentencias de control en if-elseif-else Python

#if condicion1:
# Condicon a ejecutar si
# la condicion es verdad
#elif condicion2
# codigo que se ejecuta si la condicion se cumple

#else:
# codigo que se ejecuta si el if no es verdad

print("Programa que determina tu grupo segun tu edad")
edad=input("Ingrese su edad: ")
edad=int(edad)
if edad<=14:
    print("Niños y adolesentes")
elif edad>=15 and edad<=25:
    print("Jovenes")
elif edad>=26 and edad<=45:
    print("Adultos jovenes")
elif edad>=46 and edad<=60:
    print("Adultos maduros")
else:
    print("Adultos mayores")