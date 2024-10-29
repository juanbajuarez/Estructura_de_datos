# Juan bautista Juarez
# 28  de octubre  de 2024
#Ciclo while en Python

#sintanxis
# while condicion:
#   intrucciones

#Programa que imprime un ejemplo del ciclo while ++
# ingresa un numero:
# los nmeros del 1 al {} son:
# while


print("** Programa que imprime un ejemplo del ciclo while **")
numero=input("Ingrese un numero: ")
numero=int(numero)
print(f"Los números del 1 al {numero} son: ")
contador=1
while contador<=numero:
    print(contador)
    contador+=1

print("** Programa que imprime otro ejemplo del ciclo while **")
numero=input("Ingrese un numero: ")
numero=int(numero)
print(f"Los números del 1 al {numero} son: ")
contador=1
while contador<=numero:
    print(contador,end=" ")
    contador+=1
print()
print("Fin de cuenta")

print("** Programa que imprime un ejemplo de numeros pares del ciclo while **")
numero=input("Ingrese un numero: ")
numero=int(numero)
print(f"Los números del 1 al {numero} son: ")
contador=0
while contador<=numero:
    if contador%2==0:
        print(contador,end=" ")
    contador+=1
print()
print("Fin de cuenta")