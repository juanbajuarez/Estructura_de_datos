# Juan Bautista Juárez.
# 17 de octubre de 2024.
# Ejercicio número 3 de operadores en Python. Este programa validará el usuario
# y la contraseña ingresados por el usuario.

# Declaración de cadenas como constantes.
usuario_principal = "JuanElIng"  # Declaración del usuario.
contraseña_principal = "2024-2"  # Declaración de la contraseña.

usuario = input("Ingrese su usuario: ")  # Solicita la entrada por teclado del usuario.
contraseña = input("Ingrese su contraseña: ")  # Solicita la entrada por teclado de la contraseña.

# Validación de que ambas entradas sean correctas.
validacion = (usuario == usuario_principal) and (contraseña == contraseña_principal)

# Imprime el resultado como un valor booleano.
print("¿El acceso es correcto?", validacion)