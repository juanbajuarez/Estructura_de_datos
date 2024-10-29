# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Programa que mostrará los detalles del tour turístico Ecoturixtlán

# Definición de constantes
precio_adulto = 200.00
precio_niño = 100.00
descuento = 0.10

print("*** Tour turistico Ecoturistlán ***")
# Nombre del cliente
nombre = input("Ingresa el nombre del cliente: ")

# Numero de adultos
num_adultos = int(input("Ingresa el número de adultos: "))

# Numero de niños
num_niños = int(input("Ingresa el número de niños: "))

# Día de la semana
dia = input("Ingresa el día de la semana: ")
dia=dia.lower()

# Costo sin descuentos
total = (num_adultos * precio_adulto) + (num_niños * precio_niño)

# Sentencia if para ver si esta en dia de descuento
if dia=="lunes" or dia=="martes" or dia=="jueves":
    descuento_aplicado = total * descuento
    total=total-descuento_aplicado

# Detalles de tour
print(f"Gracias por tu vista {nombre} este dia {dia}. El costo total del tour es de ${total}")

