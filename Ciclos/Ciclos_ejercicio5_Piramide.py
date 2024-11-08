# Juan bautista Juarez
# 7 de noviembre  de 2024
#Ciclo for en Python

print("Program que imprime piramides con asteriscos (*)")
tamanios=int(input("Ingrese el tamaño de la piramide: "))
contador=1
contador2=0
disenio=int(input("Ingrese el tipo de piramide que desea: "))

if disenio== 1:
    for i in range(1, tamanios+1):
        for i in range(1, contador+1):
            print("*",end=" ")
        contador+=1
        print()

elif disenio==2:
    contador=tamanios
    for i in range(1, tamanios+1):
        for i in range(1, contador+1):
            print("*",end=" ")
        contador-=1
        print()

elif disenio==3:
    contador=tamanios
    for i in range(1,tamanios+1):
        for i in range(1, contador+1):
            print("*",end=" ")
        print()
        for i in range(-1,contador2):
            print(" ",end=" ")
        contador-=1
        contador2+=1
else:

    contador3=1
    acumulador=0
    for i in range(1,tamanios+1):
        for i in range(1,acumulador+1 ):
            print(" ", end=" ")
        for i in range(1, contador3 + 1):
            print("*")
        contador3+=2
        acumulador+=1
        print()
