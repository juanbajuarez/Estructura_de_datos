'''
Juan Bautista Juarez
14 de octubre de 2024.
Descripción:
Ejercicos de conversion de datos (casting) en Python.
'''

#aConvierta los siguientes números en cadenas: 3.14159265, 12, 0.

#Declarion de mis variables a convertir
num1 = 3.14159265
num2 = 12
num3 = 0

#Conversion de numeros a cadenas
cadena1 = str(num1)
cadena2 = str(num2)
cadena3 = str(num3)
#Impresion de los datos como cadenas
print(cadena1)
print(cadena2)
print(cadena3)


# De los números anteriores, indica su valor booleano.
#Si el valor de la variables es distinto de cero se considera True
#Si el valor de la variables es igual a cero se considera False
print(bool(num1))
print(bool(num2))
print(bool(num3))

#Convierta las siguientes cadenas a números: "10002", "100.02", "0".
#Declaracion de las cadenas
cadena1 = "10002"
cadena2 = "100.02"
cadena3 = "0"

# Conversion de de cadena a entero y a flotante
num1 = int(cadena1)
num2 = float(cadena2)
num3 = int(cadena3)

print(num1)
print(num2)
print(num3)

#De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".

print(bool(cadena1))
print(bool(cadena2))
print(bool(cadena3)) #Se considera como True porque la cadena no esta vacia, aunque el valor sea cero se considera como no vacia