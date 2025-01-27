# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Descripción: Exámen tercer parcial.
# Calculadora de promedios con validación de datos
# Utilizando tuplas o diccionarios.
from promedio_modulo import menu_promedio,datos_promedio
#Código a nivel de módulo.

if __name__ == '__main__':
    seleccion=menu_promedio()
    if seleccion == 1:
        datos_promedio()
    else:
        print("Fin del programa")
