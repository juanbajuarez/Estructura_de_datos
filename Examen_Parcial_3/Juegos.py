# Autor: Juan Bautista Juárez
# Fecha: Enero de 2025
# Descripción: Exámen tercer parcial.
# Juegos en python en consola.
from gato_modulo import modos_juego
from Funciones_examen_modulo import imprimir_titulo_ahorcado
from gato_modulo import imprimir_titulo_gato
from gato_modulo import juego_del_gato
from Funciones_examen_modulo import menu_juegos



if __name__ == "__main__":
    seleccion=None
    while seleccion !=0:
        seleccion=menu_juegos()
        if seleccion==1:
            juego_del_gato()
        elif seleccion==2:
            imprimir_titulo_ahorcado()
            modos_juego()
        elif seleccion==3:
            pass

        else:
            print("Programa terminado")

