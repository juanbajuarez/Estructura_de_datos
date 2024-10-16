# Juan bautista Juarez
# 16  de octubre  de 2024
# Operadores aritmeticos compuestos en Python



numero1,numero2=input("Ingrese el primer numero: "),input("Ingrese el segundo numero: ")
numero1=int(numero1)
numero2=int(numero2)

numero1+=3   # numero1=numero1+3
numero2-=5   # numero2=numero2+5
numero1*=2   # numero1=numero1*2
numero2/=4   # numero1=numero1/4

print(numero1)
print(numero2)


numero1,numero2=input("Ingrese el primer numero: "),input("Ingrese el segundo numero: ")
numero1=int(numero1)
numero2=int(numero2)

numero1+=numero2
numero1*=numero1
numero1-=numero2
numero1+=3
numero1/=2

print(numero1)
print(numero2)
print(f"{numero1+5}") #sintaxis para operar dentro del print