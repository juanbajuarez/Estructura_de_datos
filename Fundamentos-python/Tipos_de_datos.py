'''
Juan Bautista Juarez
7 de octubre de 2024.
Descripción:
Usos de los tipos básico de datos en Python.
Se muestran los distintos tipos de datos y como se declaran
'''

# Notas:
"""
En Python, no se requiere indicar el tipo de la variable en su declaración.
Los valores básicos que pueden almacenar las variables son:
- Int
- Float
- String (str)
- Boolean. True o False (con inicial mayúscula).
- None. Tipo especial que representa una ausencia de valor.
"""

# Ejemplos de tipos de datos.

# Número entero
mi_variable_entera = -100            #Declaracion de un entero negativo
print("Tipo de dato entero:",mi_variable_entera) #Se imprime un entero negativo

# Número decimal
mi_variable_decimal = 12.12    #declaracion de un flotante
print("Tipo de dato decimal:", mi_variable_decimal)  #Se imprime un flotante

# Cadena de texto
mi_variable_texto_nombre = "Juan"  #se imprime una cadena
mi_variable_texto_apellido = 'Bautista ' #se imprime una cadena
print("Cadena de texto:", mi_variable_texto_nombre, mi_variable_texto_apellido)  #Se imprimen dos cadenas

# Booleno
mi_variable_booleana = True #declaracion de un boleano
print('Tipo booleano:', mi_variable_booleana) #se imprime un boleano

# None
mi_variable_none = None         #Se declara un none
print("Tipo none:",mi_variable_none) # Se imprime un none

# Uso de constantes.
'''
En Python, a diferencia de otros lenguajes de programación, no existe un tipo específico para definir constantes.
Se utiliza una convención de colocar las variables en mayúsculas y no modificarlas.
'''
VARIABLE_CONSTANTE = 3.1416   #Se declara una constante de tipo flotante
print("Ejemplo de convención de una constante:", VARIABLE_CONSTANTE) #Se imprime la constante flotante