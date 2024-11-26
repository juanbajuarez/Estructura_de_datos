# Juan bautista Juarez
# 7 de noviembre  de 2024
# Piramides con funciones


def forma1(a):
    contador = 1
    contador2 = 0
    for i in range(1, tamanios+1):
        for i in range(1, contador+1):
            print("*",end=" ")
        contador+=1
        print()
    print()
    print("**********************")
def forma2(a):
    contador2 = 0
    contador = tamanios
    for i in range(1, tamanios + 1):
        for i in range(1, contador + 1):
            print("*", end=" ")
        contador -= 1
        print()
    print()
    print("**********************")
def forma3(a):
    contador2 = 0
    contador = tamanios
    for i in range(1, tamanios + 1):
        for i in range(1, contador + 1):
            print("*", end=" ")
        print()
        for i in range(-1, contador2):
            print(" ", end=" ")
        contador -= 1
        contador2 += 1
    print()
    print("**********************")
def forma4(a):
    contador = 1
    contador2 = 0
    acumulador=0
    for i in range(1, acumulador + 1):
        print(" ", end=" ")
    for i in range(1, contador2 + 1):
        print("*")
    contador2 += 2
    acumulador += 1
    print()
    print("**********************")

print("Program que imprime piramides con asteriscos (*)")
tamanios=int(input("Ingrese el tamaño de la piramide: "))

forma1(tamanios)
forma2(tamanios)
forma3(tamanios)
forma4(tamanios)
print()
