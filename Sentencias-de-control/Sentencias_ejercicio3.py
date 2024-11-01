# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Programa para determinar si recibes descuento al comprar en "La Cona".

print("** Descuento por ser miembro de LA CONA **")

# Ingresa el monto de la compra
monto_compra = float(input("Ingresa la cantidad comprada en la tienda: $"))

# Pregunta si tiene membresía o no
membresia = input("¿Tiene membresía? (Si/No): ")
membresia = membresia.lower()
descuento = 0

# Sentencia if anidada para validar la membresía y el descuento aplicable
if membresia == "si":
    if monto_compra >= 1000:  # Valida si su compra es mayor a $1000
        print("El descuento es del 8%.")
        descuento = 0.08  # Se le aplica un descuento del 8%
    else:
        descuento = 0.05  # Se le aplica un descuento del 5%
        print("El descuento es del 5%.")
else:
    print("No tienes derecho a un descuento. Te invitamos a ser miembro.")

# Se aplican los descuentos correspondientes
descuento_ganado = monto_compra * descuento
total = monto_compra - descuento_ganado

# Se imprime en pantalla el precio final de la compra
print(f"Total a pagar: ${total:.2f}")
