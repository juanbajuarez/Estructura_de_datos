# Autor: Juan Bautista Juárez
# Fecha: Enero de 2024
# Descripción: Funciones Intermedio
#

def colores_favoritos(persona:str,*vargs)->None:
    print(f"{persona}:{vargs}")

def sumar(*vargs)->int:
    resultado=0
    for i in vargs:
        resultado+=i
    return resultado

if __name__ == '__main__':
    colores_favoritos("Jennifer", "Morado","Negro","Blanco","Rosa")
    colores_favoritos("Addi", "Azul","Blanco","Negro")
    colores_favoritos("Juan", "Azul")
    cadena="Hola"
    tupla="Hola",
    print(cadena)
    print(tupla)
    res=sumar(10,9,8,7,6,5,4,3,2,1)
    print(res)