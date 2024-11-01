# Juan Bautista Juárez.
# 28 de octubre de 2024.
# Programa para determinar si puedes ingresar al bar "La Negra".

print("*** Verificación de acceso al bar 'La Negra' ***")

# Se ingresa la edad de la persona.
edad = int(input("Ingresa tu edad: "))

# Se ingresa la cantidad de dinero que lleva la persona.
dinero = float(input("Ingresa el dinero con el que cuentas: $"))

# Se emplean sentencias de control y operaciones booleanas.
if edad >= 18 and dinero >= 250:
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar.")

