# Juan Bautista Juarez
# 17  de Octubre  de 2024
# Ejercicio número 1 de operadores en Python. Este programa indica si el usuario es
# acreedor a una bonificacion siempre y cuando cumpla dos condiciones, que su compra sea mayor o igual
# a 5000 y sea a meses sin intereses.

compras=float(input("Ingrese la cantidad gastada en las compras:"))
cadena1= input("Las compras fueron a meses sin interes si o no: ")
cadena1=cadena1.lower()=="si"
print(f"¿Aplica a bonificacion?{cadena1 and compras>=5000 }")