# Juan Bautista Juarez
# 15  de Octubre  de 2024
# Operadores de asignacion en Python
#asignacion multiple
numero1,numero2=5,10 #El operador ¨=¨ asigna un valor a la variable indicada.
numero3,numero4=9.14,"chuy" #Puedes asignar dos o mas valores de distinto tipo a distintas variables.
#Se imprimer los valores asignados a las variables.
print(numero1)
print(numero2)
print(numero3)
print(numero4)

numero5,numero6=numero1+numero2,numero1-numero2 #Se pueden realizar operaciones algebraicas al asignar valores.

print(numero5)
print(numero6)

#asignacion encadenada
numero7=numero8=numero9=10 #Sirve para asignar el mismo valor a distintas variables.
print(numero7)
print(numero8)
print(numero9)

#intercambio de variables.

numero10,numero11="albert","geto"

print(numero10)
print(numero11)
numero11,numero10=numero10,numero11 #Se aplica para intercambiar valores
# entre dos variables sin necesidad de una tercera valiable temporal.

print(numero10)
print(numero11)

#Entrada multiple de valores.

nombre,apellido=input("nombre: "),input("apellido: ") #Se aplica el mismo concepto
#para pedir datos por consola simultaneamente.
print(nombre)
print(apellido)