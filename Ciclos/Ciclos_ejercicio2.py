# Juan bautista Juarez
# 28  de octubre  de 2024
#Ciclo while en Python

print("** Programa que calcila la suma acumulativa entre 2 numeros **")
numero1=input("Ingrese el numero inicial: ")
numero1=int(numero1)
numero2=input("Ingrese el numero final: ")
numero2=int(numero2)

contador=numero1
acumulador=0
while contador<=numero2:
    acumulador+=contador
    contador+=1
print(f"La suma de {numero1} hasta {numero2} es: {acumulador} ")