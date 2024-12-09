# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Exámen ejercicio número 3 "Lenguaje hacker (l33t sp34k)"

"""
Por clave-valor
Ejemplos de usos
nombre_diciionarios={'key':"valor",'key2':"valor2"}
"""


#Función del menú.
def menu():
    print("***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***")
    print("1) Convertir un texto a lenguaje básico.")
    print("2) Convertir un texto a lenguaje intermedio.")
    print("0) Salir.")
    opcion=int(input("Ingresa una de las opciones: "))
    return opcion

#Función utilizando diccionario para obtener den valor l33t de las vocales
def vocales(caracter):
    l33t=caracter
    vocales={('A', 'a'): "4",('E', 'e'): "3",('I', 'i'): "1",('O', 'o'): "0",
             ('U', 'u'): "(_)",}

    for clave, valor in vocales.items():
        if l33t in clave:
            l33t=valor
    return l33t

#Función utilizando diccionario para obtener den valor l33t de las consonates.
def consonates(caracter):
    l33t = caracter
    consonates={('B', 'b'): "I3",('C', 'c'): "[", ('D', 'd'): ")",  ('F', 'f'): "|=",
                ('G', 'g'): "&", ('H', 'h'): "#", ('J', 'j'): ",_|", ('K', 'k'): ">|",
                ('L', 'l'): "1", ('M', 'm'): "(V)", ('N', 'n'): "^/",
                ('P', 'p'): "|*", ('Q', 'q'): "(_,)", ('R', 'r'): "I2", ('S', 's'): "5",
                ('T', 't'): "7", ('V', 'v'): "|/", ('W', 'w'): "uu",
                ('X', 'x'): "><", ('Y', 'y'): "`/", ('Z', 'z'): "2"}
    for clave, valor in consonates.items():
        if l33t in clave:
            l33t=valor
    return l33t

#Función lenguaje básico.
def basico(palabra):
    tam=len(palabra)
    lista_palabra=[]
    l33t=[]
    #Convierte palabra a lista
    for i in range(0,tam):
        lista_palabra.append(palabra[i])
    # Cambia vocales.
    for i in range(0,tam):
        l33t.append(vocales(lista_palabra[i]))
    for i in range(0, tam):
        print(l33t[i],end='')
    print()

#Función lenguaje intermedio.
def intermedio(palabra):
    tam=len(palabra)
    lista_palabra=[]
    lista_palabra2=[]
    l33t=[]
    # Convierte palabra a lista
    for i in range(0,tam):
        lista_palabra.append(palabra[i])
    #Cambia vocales.
    for i in range(0,tam):
        lista_palabra2.append(vocales(lista_palabra[i]))
    #Cambia consonantes.
    for i in range(0, tam):
        l33t.append(consonates(lista_palabra2[i]))
    for i in range(0, tam):
        print(l33t[i],end='')
    print()

# Código a nivel de módulo.
opcion = None
while opcion != 0:
    opcion = menu()
    if opcion==1:
         frase=input("Ingresa el texto a convertir en leguaje l33t básico: ")
         basico(frase)
    elif opcion==2:
        frase = input("Ingresa el texto a convertir en leguaje l33t intermedio: ")
        intermedio(frase)
    elif opcion<0 or opcion>2:
        print("Opción no válida.")
    else:
        print("Programa Terminado")
    print("***********************************************")