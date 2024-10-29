# Juan bautista Juarez
# 28  de octubre  de 2024
#Ciclo while en Python
#import randi(in,)

print("** Programa que calcula la suma acumulativa **")
numero=input("Ingrese un numero: ")
numero=int(numero)
contador=0
acumulador=0
while contador<=numero:
acumulador+=contador
contador+=1
print(f"La suma de 0 hasta {numero} es: {acumulador} ")