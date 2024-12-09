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

#Función que retorna el valor en decimal.
def cal_decimal(valor):
    decimal=valor
    if valor=='A' or valor=='a':
        decimal=10
    elif valor=='B' or valor=='b':
        decimal=11
    elif valor=='C' or valor=='c':
        decimal=12
    elif valor=='D' or valor=='d':
        decimal=13
    elif valor=='E' or valor=='e':
        decimal=14
    elif valor=='F' or valor=='f':
        decimal=15
    return decimal

#Función que convierte de decimal a hexadecimal.
def decimal_hexadecimal(numero):
    hexadecimal = []
    while numero != 0:
        residuo = numero % 16
        valexa = cal_hexadecimal(residuo)
        numero = numero // 16
        hexadecimal.append(valexa)
    hexadecimal.reverse()
    return hexadecimal

#Función que convierte de decimal a binario
def decimal_binario(numero):
    #conversion a binario:
    num1=numero
    binario=[]
    while num1!=0:
        residuo=num1%2
        num1=num1//2
        binario.append(residuo)
    binario.reverse()
    return binario


#Función que convierte de decimal a binario y hexadecimal.
def decimal_binario_y_hexadecimal(numero):
    #conversion a binario en función:
    #Conversion a hexadecimal en función:
    return decimal_binario(numero),decimal_hexadecimal(numero)

#Función que convierte de binario a decimal y a hexadecimal.
def binario_decimal_y_hexadecimal(numero):
    #Conversion a decimal.
    decimal=[]
    tam=len(numero)
    print(tam)
    acum=0
    for i in range(tam):
        print(i)
        acum+=int(numero[tam-1-i])*(2**i)
    decimal.append(acum)

    #Conversion a hexadecimal.
    return decimal,decimal_hexadecimal(acum)

#Función que convierte de hexadecimal a decimal y binario.
def hexadecimal_decimal_y_binario(numero):
    decimal = []
    valor_decimal=[]
    tam = len(numero)
    acum=0
    #Conversion de caracteres a enteros.
    for i in range(0,tam):
        val=cal_decimal(numero[i])
        decimal.append(val)
    #Calcula el valor decimal.
    for i in range(tam):
        acum += int(decimal[tam - 1 - i]) * (16 ** i)
    valor_decimal.append(acum)
    #El valor binario se realiza por función.
    return valor_decimal,decimal_binario(acum)

# Código a nivel de módulo.
opcion = None
while opcion != 0:
    opcion = menu()
    if opcion==1:
        numero=int(input("Ingrese el número en base decimal: "))
        tupla=decimal_binario_y_hexadecimal(numero)
        binario= ''.join(map(str, tupla[0]))
        hexa=''.join(map(str,tupla[1]))
        print(f"El número decimal {numero} es {binario} en binario y {hexa} en hexadecimal.")
    elif opcion==2:
        numero = input("Ingrese el número en base binaria: ")
        tupla=binario_decimal_y_hexadecimal(numero)
        decimal= ''.join(map(str, tupla[0]))
        hexa = ''.join(map(str, tupla[1]))
        print(f"El número binario {numero} es {decimal} en decimal y {hexa} en hexadecimal.")
    elif opcion==3:
        numero = input("Ingrese el número en base hexadecimal: ")
        tupla=hexadecimal_decimal_y_binario(numero)
        decimal = ''.join(map(str, tupla[0]))
        binario = ''.join(map(str, tupla[1]))
        print(f"El número hexadecimal {numero} es {decimal} en decimal y {binario} en binario.")
    elif opcion<0 or opcion>3:
        print("Opción no válida.")
    else:
        print("Programa Terminado")
    print()
    print("************************************************************************")

