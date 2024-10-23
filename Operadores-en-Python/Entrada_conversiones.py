# Juan Bautista Juarez
# 21  de Octubre  de 2024
# Conversión de cadenas a int, float y
# boolean mediante la interacción con consola.

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****") #Imprime el mesaje en consola.
nombre = input("Ingresa el nombre: ") #Pide que ingrese el nombre del alumno por consola.
#La instruccion mas interna indica que sera una entrada por consola y la segunda instrucción
# hace referencia al tipo de dato de como sera guardado.
semestre = int(input("Ingresa el no. de semestre: ")) #Indica que pide un numero entero por consola.
promedio = float(input("Ingresa el promedio: ")) #Indica que pide un numero booleano por consola.
es_mujer = input("¿Es mujer (Si/No)?: ")#Pide una cadena como estrada.


# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")
# {promedio:.2f} Esta linea es para indicar que se impriman dos decimales como formato al valor de promedio.