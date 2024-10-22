# Juan Bautista Juarez
# 16  de Octubre  de 2024
# Operadores relacionales en Python

#Entrada por consola de dos numeros enteros.
numero1,numero2=input("Ingrese el primer numero: "),input("Ingrese el segundo numero: ")
#Conversion de entero a flotante
numero1=float(numero1)
numero2=float(numero2)

#Operaciones entre variables que imprimen un valor booleano.
print(f"¿El {numero1:.2f} es mayor que el {numero2:.2f}?{numero1>numero2}") #EL primer número es mayor que el segundo.
print(f"¿El {numero1:.2f} es mayor o igual que el {numero2:.2f}?{numero1>=numero2}") #EL primer número es mayor o igual que el segundo.
print(f"¿Los numeros son iguales?{numero1==numero2}") #Los dos numeros son iguales.
print(f"¿El {numero1:.2f} es menor que el {numero2:.2f}?{numero1<numero2}")#EL primero número es menor que el segundo.
print(f"¿El {numero1:.2f} es menor o igual que el {numero2:.2f}?{numero1<=numero2}")#El primer número es menor o igual que el seg undp.
print(f"¿Los numeros son diferentes?{numero1!=numero2}")#EL primer número es diferente del segundo.