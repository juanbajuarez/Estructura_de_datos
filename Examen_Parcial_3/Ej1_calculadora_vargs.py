# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Descripción: Exámen tercer parcial.
# Calculadora con validación de datos.

from Funciones_examen_modulo import menu_calculadora
from Funciones_examen_modulo import suma
from Funciones_examen_modulo import multiplicacion
#Código a nivel de módulo.

if __name__ == '__main__':
    opcion=None
    while opcion!=0:
        opcion = menu_calculadora()
        if opcion==1:
            suma()
        elif opcion==2:
            multiplicacion()
        else:
            print("Fin del programa")

