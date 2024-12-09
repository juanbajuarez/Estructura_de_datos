# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Exámen ejercicio número 2 "Convesiones"

#Función del menú.
def menu():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("1) Convertir de decimal a binario y hexadecimal.")
    print("2) Convertir de binario a decimal y hexadecimal.")
    print("3) Convertir de hexadecimal a decimal y binario.")
    print("0) Salir.")
    opcion=int(input("Ingresa una de las opciones: "))
    return opcion

#Función que retorna el valor en hexadecimal.
def cal_hexadecimal(numero):
    hexa=numero
    if numero==10:
        hexa='A'
    elif numero==11:
        hexa='B'
    elif numero==12:
        hexa='C'
    elif numero==13:
        hexa='D'
    elif numero==14:
        hexa='E'
    elif numero==15:
        hexa='F'
    return hexa

#Función que convierte de decimal hexadecimal.
def decimal_hexadecimal(numero):
    hexadecimal = []
    while numero != 0:
        residuo = numero % 16
        valexa = cal_hexadecimal(residuo)
        numero = numero // 16
        hexadecimal.append(valexa)
    hexadecimal.reverse()
    return hexadecimal

#Función que convierte de decimal a binario y hexadecimal.
def decimal_binario_y_hexadecimal(numero):
    #conversion a binario:
    num1=numero
    binario=[]
    while num1!=0:
        residuo=num1%2
        num1=num1//2
        binario.append(residuo)
    binario.reverse()

    #Conversion a hexadecimal:

    return binario,decimal_hexadecimal(numero)

#Función que convierte de binario a decimal y a hexadecimal.
def binario_decimal_y_hexadecimal(numero):
    #Conversion a decimal.
    decimal=[]
    tam=len(numero)
    print(tam)
    acum=0
    for i in range(tam):
        acum+=int(numero[tam-1-i])*(2**i)
    decimal.append(acum)

    #Conversion a hexadecimal.
    return decimal,decimal_hexadecimal(acum)

#Función que convierte de hexadecimal a decimal y binario.
def hexadecimal_decimal_y_binario(numero):
    print()

# Código a nivel de módulo.
opcion = None
while opcion != 0:
    opcion = menu()
    if opcion==1:
        numero=int(input("Ingrese el número en base decimal: "))
        tupla=decimal_binario_y_hexadecimal(numero)
        binario= ''.join(map(str, tupla[0]))
        hexa=''.join(map(str,tupla[1]))
        print(f"El número {numero} es {binario} en binario y {hexa} en hexadecimal.")
    elif opcion==2:
        numero = input("Ingrese el número en base binaria: ")
        tupla=binario_decimal_y_hexadecimal(numero)
        decimal= ''.join(map(str, tupla[0]))
        hexa = ''.join(map(str, tupla[1]))
        print(f"El número {numero} es {decimal} en decimal y {hexa} en hexadecimal.")
    elif opcion==3:
        numero = input("Ingrese el número en base hexadecimal: ")
        tupla=hexadecimal_decimal_y_binario(numero)
        decimal = ''.join(map(str, tupla[0]))
        binario = ''.join(map(str, tupla[1]))
        print(f"El número {numero} es {decimal} en decimal y {binario} en binario.")
    elif opcion<0 or opcion>3:
        print("Opción no válida.")
    else:
        print("Programa Terminado")

