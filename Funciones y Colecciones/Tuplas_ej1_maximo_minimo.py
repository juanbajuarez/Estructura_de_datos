# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza funciones con tuplas
# para implementar el control de calificaciones de un grupo.


# Función que muestra el menú.
def menu():
    print("1) Ver lista de números.")
    print("2) Añadir número a la lista.")
    print("3) Determinar el valor máximo y mínimo de la lista de números.")
    print("0) Salir.")

# Función que retorna una tupla con el valor mínimo y máximo de la lista.
def valores_M(numeros):
    num_minimo=numeros[0]
    num_maximo=numeros[0]
    for numero in numeros:
        if numero>num_maximo:
            num_maximo=numero
        if numero<num_minimo:
            num_minimo = numero
    return num_minimo,num_maximo

#Código a nivel de módulo.
opcion=None
numeros=[]
while opcion!=0:
    print("*** Valor máximo y mínimo de una lista de números del usuario ***")
    menu()
    opcion=int(input("Ingrese una opción: "))
    if opcion==1:
        if len(numeros)==0:
            print("No hay números para mostrar. ")
        else:
            print(numeros)
    elif opcion==2:
        numero_ingresado=float(input("Ingrese un número: "))
        numeros.append(numero_ingresado)

    elif opcion ==3:
        if len(numeros)==0:
            print("No hay números para mostrar.")
        else:
            tupla_valores=valores_M(numeros)
            print(f"El valor minimo de la lista es: {tupla_valores[0]} y el valor máximo es: {tupla_valores[1]}")
    else:
        print("Programa terminado")
    print("***********************************************")
