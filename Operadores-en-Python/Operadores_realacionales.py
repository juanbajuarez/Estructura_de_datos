# Juan bautista Juarez
# 16  de octubre  de 2024
# Se utilizan para comparar dos valor en Python

numero1,numero2=input("Ingrese el primer numero: "),input("Ingrese el segundo numero: ")
numero1=float(numero1)
numero2=float(numero2)

print(f"¿El {numero1:.2f} es mayor que el {numero2:.2f}?{numero1>numero2}")
print(f"¿El {numero1:.2f} es mayor o igual que el {numero2:.2f}?{numero1>=numero2}")
print(f"¿Los numeros son iguales?{numero1==numero2}")
print(f"¿El {numero1:.2f} es menor que el {numero2:.2f}?{numero1<numero2}")
print(f"¿El {numero1:.2f} es menor o igual que el {numero2:.2f}?{numero1<=numero2}")
print(f"¿Los numeros son diferentes?{numero1!=numero2}")